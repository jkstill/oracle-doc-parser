"""
oracle_rag.backends
~~~~~~~~~~~~~~~~~~~
LLM backend integrations for the oracle-rag ask command.

Supported backends:
  - Ollama (local or remote, via HTTP API)
  - Gemini CLI (via subprocess)
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

    backend: 'ollama' | 'gemini'
    """
    if backend == "ollama":
        if not ollama_url:
            raise ValueError("--ollama-url is required for the ollama backend")
        if not model:
            raise ValueError("--model is required for the ollama backend")
        return OllamaBackend(ollama_url, model, timeout=timeout)

    if backend == "gemini":
        return GeminiCLIBackend(cli_path=gemini_cli, model=model, timeout=timeout)

    raise ValueError(f"Unknown backend: {backend!r}. Choose 'ollama' or 'gemini'.")
