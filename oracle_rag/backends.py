"""
oracle_rag.backends
~~~~~~~~~~~~~~~~~~~
LLM backend integrations for the oracle-rag ask command.

Supported backends:
  - ollama     OllamaBackend      — local or remote Ollama server (HTTP API)
  - gemini     GeminiCLIBackend   — Gemini CLI via subprocess (free tier)
  - claude     ClaudeCLIBackend   — Claude CLI via subprocess (free, uses Claude.ai subscription)
  - claude-api ClaudeAPIBackend   — Anthropic API direct (paid, per-token billing)

Each backend's generate() method returns a GenerationResult containing
the response text plus timing and token usage stats.
"""

from __future__ import annotations

import json
import subprocess
import time
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Result dataclass — common across all backends
# ---------------------------------------------------------------------------

@dataclass
class GenerationResult:
    """
    Response from an LLM backend, with timing and token usage.

    Token counts:
      - Ollama:   exact (returned by API)
      - Claude:   exact (returned by API)
      - Gemini:   estimated (~4 chars per token, standard approximation)
    """
    text:          str
    elapsed_sec:   float
    input_tokens:  int
    output_tokens: int
    exact_tokens:  bool   # True if token counts are from the API, False if estimated

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens

    def stats_line(self) -> str:
        """Single-line summary for display."""
        approx = "" if self.exact_tokens else " (est)"
        return (
            f"tokens: {self.input_tokens} in / {self.output_tokens} out / "
            f"{self.total_tokens} total{approx}  |  "
            f"time: {self.elapsed_sec:.1f}s"
        )


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 characters per token."""
    return max(1, len(text) // 4)


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class LLMBackend(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> GenerationResult:
        """Send prompt, return GenerationResult."""
        ...

    @abstractmethod
    def name(self) -> str:
        ...


# ---------------------------------------------------------------------------
# Ollama backend
# ---------------------------------------------------------------------------

class OllamaBackend(LLMBackend):
    """
    Calls the Ollama HTTP API directly — works for local or remote servers.

    Args:
        base_url: Ollama server URL, e.g. 'http://lestrade:11434'
        model:    Model name, e.g. 'qwen2.5:14b', 'llama3', 'mistral'
        timeout:  Request timeout in seconds (default 120)
    """

    def __init__(self, base_url: str, model: str, timeout: int = 120):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def name(self) -> str:
        return f"ollama/{self.model} @ {self.base_url}"

    def list_models(self) -> list[str]:
        """Return list of available model names on the server."""
        url = f"{self.base_url}/api/tags"
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                data = json.loads(resp.read())
                return [m["name"] for m in data.get("models", [])]
        except Exception as e:
            raise ConnectionError(f"Cannot reach Ollama at {self.base_url}: {e}") from e

    def generate(self, prompt: str) -> GenerationResult:
        url = f"{self.base_url}/api/generate"
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }).encode("utf-8")

        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        t0 = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read())
        except urllib.error.URLError as e:
            raise ConnectionError(
                f"Ollama request failed at {self.base_url}: {e}"
            ) from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Unexpected response from Ollama: {e}") from e

        elapsed = time.monotonic() - t0
        text = data.get("response", "").strip()

        # Ollama returns exact token counts
        input_tokens  = data.get("prompt_eval_count", _estimate_tokens(prompt))
        output_tokens = data.get("eval_count", _estimate_tokens(text))

        return GenerationResult(
            text=text,
            elapsed_sec=elapsed,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            exact_tokens=True,
        )


# ---------------------------------------------------------------------------
# Gemini CLI backend
# ---------------------------------------------------------------------------

class GeminiCLIBackend(LLMBackend):
    """
    Calls the Gemini CLI via subprocess.
    Assumes `gemini` is on PATH and configured with credentials.
    Token counts are estimated since the CLI doesn't report them.

    Args:
        cli_path: Path to the gemini binary (default: 'gemini')
        model:    Model to use, passed as --model flag if set
        timeout:  Subprocess timeout in seconds (default 120)
    """

    def __init__(
        self,
        cli_path: str = "gemini",
        model: Optional[str] = None,
        timeout: int = 120,
    ):
        self.cli_path = cli_path
        self.model = model
        self.timeout = timeout

    def name(self) -> str:
        m = f"/{self.model}" if self.model else ""
        return f"gemini-cli{m}"

    def generate(self, prompt: str) -> GenerationResult:
        cmd = [self.cli_path]
        if self.model:
            cmd += ["--model", self.model]

        t0 = time.monotonic()
        try:
            result = subprocess.run(
                cmd,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
        except FileNotFoundError:
            raise RuntimeError(
                f"Gemini CLI not found at '{self.cli_path}'. "
                "Ensure it is installed and on PATH."
            )
        except subprocess.TimeoutExpired:
            raise TimeoutError(f"Gemini CLI timed out after {self.timeout}s")

        elapsed = time.monotonic() - t0

        if result.returncode != 0:
            err = result.stderr.strip()
            raise RuntimeError(f"Gemini CLI exited {result.returncode}: {err}")

        text = result.stdout.strip()

        return GenerationResult(
            text=text,
            elapsed_sec=elapsed,
            input_tokens=_estimate_tokens(prompt),
            output_tokens=_estimate_tokens(text),
            exact_tokens=False,
        )


# ---------------------------------------------------------------------------
# Claude CLI backend
# ---------------------------------------------------------------------------

class ClaudeCLIBackend(LLMBackend):
    """
    Calls the Claude CLI via subprocess — free, uses Claude.ai subscription.
    Assumes `claude` is on PATH and authenticated.

    The Claude CLI reads the prompt from stdin when passed the -p flag,
    which suppresses the interactive REPL and returns the response on stdout.

    Args:
        cli_path: Path to the claude binary (default: 'claude')
        model:    Model to use, passed as --model flag if set
        timeout:  Subprocess timeout in seconds (default 120)
    """

    def __init__(
        self,
        cli_path: str = "claude",
        model: Optional[str] = None,
        timeout: int = 120,
    ):
        self.cli_path = cli_path
        self.model = model
        self.timeout = timeout

    def name(self) -> str:
        m = f"/{self.model}" if self.model else ""
        return f"claude-cli{m}"

    def generate(self, prompt: str) -> GenerationResult:
        # -p sends a single prompt non-interactively and exits
        cmd = [self.cli_path, "-p", prompt]
        if self.model:
            cmd += ["--model", self.model]

        t0 = time.monotonic()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
        except FileNotFoundError:
            raise RuntimeError(
                f"Claude CLI not found at '{self.cli_path}'. "
                "Install it from https://claude.ai/download or ensure it is on PATH."
            )
        except subprocess.TimeoutExpired:
            raise TimeoutError(f"Claude CLI timed out after {self.timeout}s")

        elapsed = time.monotonic() - t0

        if result.returncode != 0:
            err = result.stderr.strip()
            raise RuntimeError(f"Claude CLI exited {result.returncode}: {err}")

        text = result.stdout.strip()

        return GenerationResult(
            text=text,
            elapsed_sec=elapsed,
            input_tokens=_estimate_tokens(prompt),
            output_tokens=_estimate_tokens(text),
            exact_tokens=False,
        )


# ---------------------------------------------------------------------------
# Claude API backend
# ---------------------------------------------------------------------------

class ClaudeAPIBackend(LLMBackend):
    """
    Calls the Anthropic Claude API directly via HTTP (paid, per-token billing).

    Requires the ANTHROPIC_API_KEY environment variable to be set.

    Args:
        model:   Claude model string, e.g. 'claude-haiku-4-5-20251001'
                 Default: 'claude-haiku-4-5-20251001'
        timeout: Request timeout in seconds (default 120)
    """

    API_URL = "https://api.anthropic.com/v1/messages"
    DEFAULT_MODEL = "claude-haiku-4-5-20251001"

    def __init__(self, model: Optional[str] = None, timeout: int = 120):
        import os
        self.model = model or self.DEFAULT_MODEL
        self.timeout = timeout
        self.api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is not set. "
                "Export it before using the claude backend:\n"
                "  export ANTHROPIC_API_KEY=sk-ant-..."
            )

    def name(self) -> str:
        return f"claude-api/{self.model}"

    def list_models(self) -> list[str]:
        """Return list of available Claude model IDs."""
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/models",
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                return [m["id"] for m in data.get("data", [])]
        except Exception as e:
            raise ConnectionError(f"Cannot reach Claude API: {e}") from e

    def generate(self, prompt: str) -> GenerationResult:
        payload = json.dumps({
            "model": self.model,
            "max_tokens": 4096,
            "messages": [
                {"role": "user", "content": prompt}
            ],
        }).encode("utf-8")

        req = urllib.request.Request(
            self.API_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        t0 = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            try:
                err = json.loads(body)
                msg = err.get("error", {}).get("message", body)
            except json.JSONDecodeError:
                msg = body
            raise RuntimeError(f"Claude API error {e.code}: {msg}") from e
        except urllib.error.URLError as e:
            raise ConnectionError(f"Claude API request failed: {e}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Unexpected response from Claude API: {e}") from e

        elapsed = time.monotonic() - t0

        blocks = data.get("content", [])
        text = "\n".join(
            b["text"] for b in blocks if b.get("type") == "text"
        ).strip()

        # Claude API returns exact token counts in "usage"
        usage = data.get("usage", {})
        input_tokens  = usage.get("input_tokens",  _estimate_tokens(prompt))
        output_tokens = usage.get("output_tokens", _estimate_tokens(text))

        return GenerationResult(
            text=text,
            elapsed_sec=elapsed,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            exact_tokens=True,
        )


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def make_backend(
    backend: str,
    ollama_url: Optional[str] = None,
    model: Optional[str] = None,
    gemini_cli: str = "gemini",
    claude_cli: str = "claude",
    timeout: int = 120,
) -> LLMBackend:
    """
    Factory function — create a backend from CLI args.

    backend: 'ollama' | 'gemini' | 'claude' | 'claude-api'
      ollama     — Ollama HTTP API (local or remote)
      gemini     — Gemini CLI via subprocess (free)
      claude     — Claude CLI via subprocess (free, Claude.ai subscription)
      claude-api — Anthropic API direct (paid, requires ANTHROPIC_API_KEY)
    """
    if backend == "ollama":
        if not ollama_url:
            raise ValueError("--ollama-url is required for the ollama backend")
        if not model:
            raise ValueError("--model is required for the ollama backend")
        return OllamaBackend(ollama_url, model, timeout=timeout)

    if backend == "gemini":
        return GeminiCLIBackend(cli_path=gemini_cli, model=model, timeout=timeout)

    if backend == "claude":
        return ClaudeCLIBackend(cli_path=claude_cli, model=model, timeout=timeout)

    if backend == "claude-api":
        return ClaudeAPIBackend(model=model, timeout=timeout)

    raise ValueError(
        f"Unknown backend: {backend!r}. "
        "Choose 'ollama', 'gemini', 'claude', or 'claude-api'."
    )
