import sys
from datetime import datetime

from getSolution import get_solution
from url_registry import get_selected_entries
from utils import getFileFromLink, newDriver


def _human_age(delta):
    total_seconds = int(delta.total_seconds())
    if total_seconds < 60:
        return f"{total_seconds}s ago"
    if total_seconds < 3600:
        return f"{total_seconds // 60}m ago"
    if total_seconds < 86400:
        return f"{total_seconds // 3600}h ago"
    return f"{total_seconds // 86400}d ago"


def _print_database_status(url_id, url):
    file_path = getFileFromLink(url)

    if not file_path.exists():
        print(f"[{url_id}] {url}")
        print(f"    Database file missing: {file_path.name}")
        print("    Run ./load.sh to create or update this database file.")
        return False

    modified_at = datetime.fromtimestamp(file_path.stat().st_mtime)
    age = datetime.now() - modified_at
    print(f"[{url_id}] {url}")
    print(f"    Database last updated: {modified_at.strftime('%Y-%m-%d %H:%M:%S')} ({_human_age(age)})")
    return True


def run(selected_ids=None):
    selected_entries = get_selected_entries(selected_ids or [])

    if not selected_entries:
        print("No valid URL IDs were provided. Nothing to run.")
        return

    print(f"Running {len(selected_entries)} URL(s)...")

    for url_id, url in selected_entries:
        if not _print_database_status(url_id, url):
            continue

        options, driver, wait = newDriver(url, headless=False)
        get_solution(options, driver, wait, url)
        driver.quit()


run(sys.argv[1:])