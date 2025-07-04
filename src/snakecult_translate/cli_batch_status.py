#!/usr/bin/env python3
"""
cli_batch_status.py
===================

Utility CLI to inspect the status of previously-submitted OpenAI Batch API jobs
used by the snakecult_translate system.

It scans the local **batch_work/** directory for mapping files created by
`cli_batch_async.py`, extracts the batch-id, queries the OpenAI API for the
current status (in_progress/completed/failed), and prints a compact table.

Example usages
--------------

1. One-off status snapshot (no API polling):

    python -m src.snakecult_translate.cli_batch_status

2. Continuous watch every 60 s until all batches are completed:

    python -m src.snakecult_translate.cli_batch_status --watch --interval 60

3. Download & assemble a finished batch into Markdown files:

    python -m src.snakecult_translate.cli_batch_status --assemble <batch_id>

If **--assemble** is supplied without a batch-id, the script will automatically
assemble every batch that has reached the *completed* state but does not yet
have its translations on disk.

"""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

from openai import OpenAI

from .utils import load_env_and_key

BATCH_WORK_DIR = Path("batch_work")
STATUS_EMOJIS = {
    "in_progress": "⏳",
    "completed": "✅",
    "failed": "❌",
    "expired": "⌛️",
}


def parse_batch_id(mapping_file: Path) -> Optional[str]:
    """Extract the batch_id from filenames like 'batch_batch_<id>_mapping.json'."""
    m = re.match(r"batch_batch_([\w-]+)_mapping\.json", mapping_file.name)
    if m:
        captured = m.group(1)
        # Ensure returned id begins with 'batch_'
        return captured if captured.startswith("batch_") else f"batch_{captured}"
    return None


def list_mapping_files() -> List[Path]:
    if not BATCH_WORK_DIR.exists():
        return []
    return sorted(BATCH_WORK_DIR.glob("batch_batch_*_mapping.json"))


def fetch_status(client: OpenAI, batch_id: str) -> Dict[str, str]:
    try:
        batch = client.batches.retrieve(batch_id)
        return {
            "status": batch.status,
            "output_file_id": getattr(batch, "output_file_id", None),
            "error_file_id": getattr(batch, "error_file_id", None),
        }
    except Exception as e:
        return {"status": f"error: {e}"}


def assemble_batch(batch_id: str):
    """Invoke cli_batch_async --resume programmatically to download outputs."""
    cmd = [
        sys.executable,
        "-m",
        "src.snakecult_translate.cli_batch_async",
        "--resume",
        "--batch-id",
        batch_id,
    ]
    print(f"\n➡️  Assembling completed batch {batch_id} …")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to assemble batch {batch_id}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Check status of OpenAI Batch jobs created by snakecult_translate.")

    parser.add_argument("batch_ids", nargs="*", help="Specific batch-ids to query. If omitted, all local batches are checked.")
    parser.add_argument("--watch", action="store_true", help="Poll repeatedly until all queried batches complete.")
    parser.add_argument("--interval", type=int, default=60, help="Polling interval in seconds (with --watch).")
    parser.add_argument("--assemble", nargs="?", const="AUTO", metavar="BATCH_ID", help="When a batch is completed, download & assemble its outputs. If a specific batch_id is given, only assemble that one. If omitted, assemble any completed batch without outputs.")

    args = parser.parse_args()

    api_key = load_env_and_key()
    if not api_key:
        print("OPENAI_API_KEY not found.")
        sys.exit(1)
    client = OpenAI(api_key=api_key)

    # Determine which batches to inspect
    if args.batch_ids:
        batch_ids = args.batch_ids
    else:
        batch_ids = [parse_batch_id(p) for p in list_mapping_files()]
        batch_ids = [bid for bid in batch_ids if bid]

    if not batch_ids:
        print("No batch mapping files found.")
        sys.exit(0)

    def show_once():
        summaries = []
        for bid in batch_ids:
            info = fetch_status(client, bid)
            emoji = STATUS_EMOJIS.get(info["status"], "❔")
            summaries.append(f"{emoji} {bid} → {info['status']}")

            # Auto-assemble logic
            if args.assemble:
                should_assemble = False
                if args.assemble == "AUTO":
                    # Assemble any completed batch
                    should_assemble = info["status"] == "completed"
                elif args.assemble == bid:
                    should_assemble = info["status"] == "completed"
                if should_assemble:
                    assemble_batch(bid)
        print("\n".join(summaries))
        return all(fetch_status(client, bid)["status"] == "completed" for bid in batch_ids)

    completed = show_once()
    while args.watch and not completed:
        time.sleep(args.interval)
        completed = show_once()


if __name__ == "__main__":
    main() 