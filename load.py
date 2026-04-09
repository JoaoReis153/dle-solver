import sys

from getNames import write_database
from url_registry import get_selected_entries


def run(selected_ids=None):
    selected_entries = get_selected_entries(selected_ids or [])

    if not selected_entries:
        print("No valid URL IDs were provided. Nothing to load.")
        return

    print(f"Loading database for {len(selected_entries)} URL(s)...")

    for url_id, url in selected_entries:
        print(f"[{url_id}] {url}")
        write_database(url)


run(sys.argv[1:])
