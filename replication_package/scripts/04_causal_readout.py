#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PACKAGE_ROOT / "source_scripts"


def main() -> int:
    command = [sys.executable, str(SOURCE_ROOT / "build_causal_readout_memo_v2.py")]
    print("Running:", " ".join(command), flush=True)
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())