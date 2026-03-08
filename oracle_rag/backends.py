"""
oracle_rag.backends
~~~~~~~~~~~~~~~~~~~
LLM backend integrations for the oracle-rag ask command.

Supported backends:
  - Ollama (local or remote, via HTTP API)
  - Gemini CLI (via subprocess)
  - Claude (Anthropic API, requires ANTHROPIC_API_KEY)
"""

from __future__ import annotations

import json
import subprocess
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from typing import Optional


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class LLMBackend(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Send prompt, return response text."""
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

    def generate(self, prompt: str) -> str:
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
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read())
                return data.get("response", "").strip()
        except urllib.error.URLError as e:
            raise ConnectionError(
                f"Ollama request failed at {self.base_url}: {e}"
            ) from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Unexpected response from Ollama: {e}") from e


# ---------------------------------------------------------------------------
# Gemini CLI backend
# ---------------------------------------------------------------------------

class GeminiCLIBackend(LLMBackend):
    """
    Calls the Gemini CLI via subprocess.
    Assumes `gemini` is on PATH and configured with credentials.

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

    def generate(self, prompt: str) -> str:
        cmd = [self.cli_path]
        if self.model:
            cmd += ["--model", self.model]
        # Gemini CLI reads prompt from stdin
        try:
            result = subprocess.run(
                cmd,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
            if result.returncode != 0:
                err = result.stderr.strip()
                raise RuntimeError(f"Gemini CLI exited {result.returncode}: {err}")
            return result.stdout.strip()
        except FileNotFoundError:
            raise RuntimeError(
                f"Gemini CLI not found at '{self.cli_path}'. "
                "Ensure it is installed and on PATH."
            )
        except subprocess.TimeoutExpired:
            raise TimeoutError(f"Gemini CLI timed out after {self.timeout}s")



# ---------------------------------------------------------------------------
# Claude (Anthropic) backend
# ---------------------------------------------------------------------------

class ClaudeBackend(LLMBackend):
    """
    Calls the Anthropic Claude API directly via HTTP.

    Requires the ANTHROPIC_API_KEY environment variable to be set.

    Args:
        model:   Claude model string, e.g. 'claude-sonnet-4-6'
                 Default: 'claude-sonnet-4-6'
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
        return f"claude/{self.model}"


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

    def generate(self, prompt: str) -> str:
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
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read())
                # Response: {"content": [{"type": "text", "text": "..."}], ...}
                blocks = data.get("content", [])
                return "\n".join(
                    b["text"] for b in blocks if b.get("type") == "text"
                ).strip()
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

# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def make_backend(
    backend: str,
    ollama_url: Optional[str] = None,
    model: Optional[str] = None,
    gemini_cli: str = "gemini",
    timeout: int = 120,
) -> LLMBackend:
    """
    Factory function — create a backend from CLI args.

    backend: 'ollama' | 'gemini' | 'claude'
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
        return ClaudeBackend(model=model, timeout=timeout)

    raise ValueError(f"Unknown backend: {backend!r}. Choose 'ollama', 'gemini', or 'claude'.")
