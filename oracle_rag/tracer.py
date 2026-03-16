"""
oracle_rag.tracer
~~~~~~~~~~~~~~~~~
Lightweight step-by-step tracer that writes timing information to a
timestamped file in a configurable directory.

Usage::

    from oracle_rag.tracer import Tracer

    with Tracer("./trace") as t:
        t.step("start", "question=show sessions")
        # ... do work ...
        t.step("retrieval complete", "chunks=5  elapsed=0.12s")
"""

from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path
from typing import Optional


class Tracer:
    """
    Records named execution steps with cumulative and per-step timing.

    Each Tracer instance creates one file:
        <trace_dir>/trace_<YYYYMMDD_HHMMSS>.txt

    Args:
        trace_dir: Directory to write trace files (created if absent).
    """

    def __init__(self, trace_dir: str = "./trace"):
        self._dir = Path(trace_dir)
        self._dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._path = self._dir / f"trace_{ts}.txt"
        self._t0 = time.monotonic()
        self._last = self._t0
        with open(self._path, "w") as fh:
            fh.write("Oracle RAG Trace\n")
            fh.write(f"Started : {datetime.now().isoformat()}\n")
            fh.write(f"File    : {self._path}\n")
            fh.write("-" * 60 + "\n\n")

    @property
    def path(self) -> Path:
        return self._path

    def step(
        self,
        name: str,
        details: str = "",
        elapsed: Optional[float] = None,
    ) -> None:
        """
        Record a named step.

        Args:
            name:    Short label for this step.
            details: Optional extra information written on indented lines.
            elapsed: Explicit step duration.  When omitted the time since the
                     previous step() call (or __init__) is used.
        """
        now = time.monotonic()
        since_start = now - self._t0
        step_time = elapsed if elapsed is not None else (now - self._last)
        self._last = now

        with open(self._path, "a") as fh:
            fh.write(f"[{since_start:8.3f}s] {name}  (step: {step_time:.3f}s)\n")
            if details:
                for line in details.splitlines():
                    fh.write(f"             {line}\n")

    def close(self, summary: str = "") -> None:
        """Write footer with total elapsed time."""
        total = time.monotonic() - self._t0
        with open(self._path, "a") as fh:
            fh.write("\n" + "-" * 60 + "\n")
            fh.write(f"Ended   : {datetime.now().isoformat()}\n")
            fh.write(f"Total   : {total:.3f}s\n")
            if summary:
                fh.write(f"Summary : {summary}\n")

    def __enter__(self) -> "Tracer":
        return self

    def __exit__(self, *_) -> None:
        self.close()
