#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = PACKAGE_ROOT / "replication_check_log_v1.md"
REQUIRED_PATHS = [
    PACKAGE_ROOT / "README.md",
    PACKAGE_ROOT / "requirements.txt",
    PACKAGE_ROOT / "scripts" / "01_causal_models.py",
    PACKAGE_ROOT / "scripts" / "02_severity_components.py",
    PACKAGE_ROOT / "scripts" / "03_robustness.py",
    PACKAGE_ROOT / "scripts" / "04_causal_readout.py",
    PACKAGE_ROOT / "scripts" / "05_replication_checks.py",
    PACKAGE_ROOT / "source_scripts" / "_causal_modeling_runtime_v1.py",
    PACKAGE_ROOT / "source_scripts" / "dml_estimation_track1_per_cell.py",
    PACKAGE_ROOT / "data" / "processed" / "modeling_inputs_v1" / "narrator_model_matrix_main_v1.csv",
    PACKAGE_ROOT / "data" / "processed" / "video_first_post_vm_batch1_v2" / "narrator_llm_fulltext_2d_outcomes_v2.csv",
    PACKAGE_ROOT / "models" / "causal_estimates_v1" / "track1_per_cell_v1" / "track1_per_cell_estimates_v1.csv",
    PACKAGE_ROOT / "models" / "causal_estimates_v1" / "track2_v1" / "track2_estimates_v1.csv",
    PACKAGE_ROOT / "models" / "causal_estimates_v1" / "causal_estimates_readout_memo_v2.md",
    PACKAGE_ROOT / "weights" / "combined_weight_design_v1.csv",
    PACKAGE_ROOT / "robustness" / "causal_robustness_v1" / "robustness_summary_v1.md",
    PACKAGE_ROOT / "appendix" / "data_sharing_audit_v1.md",
    PACKAGE_ROOT / "appendix" / "data_availability_statement_v1.md",
    PACKAGE_ROOT / "appendix" / "replication_archive_manifest.md",
]
DISALLOWED_PATHS = [
    PACKAGE_ROOT / "data" / "processed" / "transcripts",
    PACKAGE_ROOT / "data" / "processed" / "video_first_post_vm_batch1_v2" / "segment_llm_fulltext_2d_outcomes_v2.csv",
]
HASH_TARGETS = [
    PACKAGE_ROOT / "data" / "processed" / "modeling_inputs_v1" / "narrator_model_matrix_main_v1.csv",
    PACKAGE_ROOT / "data" / "processed" / "video_first_post_vm_batch1_v2" / "narrator_llm_fulltext_2d_outcomes_v2.csv",
    PACKAGE_ROOT / "models" / "causal_estimates_v1" / "track1_per_cell_v1" / "track1_per_cell_estimates_v1.csv",
    PACKAGE_ROOT / "models" / "causal_estimates_v1" / "track2_v1" / "track2_estimates_v1.csv",
    PACKAGE_ROOT / "weights" / "combined_weight_design_v1.csv",
    PACKAGE_ROOT / "robustness" / "causal_robustness_v1" / "robustness_summary_v1.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    missing = [path for path in REQUIRED_PATHS if not path.exists()]
    forbidden = [path for path in DISALLOWED_PATHS if path.exists()]

    lines = [
        "# Replication Check Log v1",
        "",
        f"Generated: {timestamp}",
        "",
        "## Required Inventory",
        "",
    ]
    for path in REQUIRED_PATHS:
        status = "present" if path.exists() else "missing"
        lines.append(f"- {path.relative_to(PACKAGE_ROOT).as_posix()}: {status}")

    lines.extend([
        "",
        "## Exclusion Checks",
        "",
    ])
    for path in DISALLOWED_PATHS:
        status = "not present" if not path.exists() else "present (unexpected)"
        lines.append(f"- {path.relative_to(PACKAGE_ROOT).as_posix()}: {status}")

    lines.extend([
        "",
        "## Hash Inventory",
        "",
    ])
    for path in HASH_TARGETS:
        if path.exists():
            lines.append(f"- {path.relative_to(PACKAGE_ROOT).as_posix()}: `{sha256(path)}`")

    verdict = "pass" if not missing and not forbidden else "fail"
    lines.extend([
        "",
        "## Verdict",
        "",
        f"- required inventory missing: {len(missing)}",
        f"- forbidden payloads present: {len(forbidden)}",
        f"- overall verdict: {verdict}",
        "",
    ])

    LOG_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {LOG_PATH}")
    if verdict != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())