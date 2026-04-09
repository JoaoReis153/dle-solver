import sys

from getNames import write_database
from getSolution import get_solution
from utils import newDriver


URLS_BY_ID = {
    1: "https://dotadle.net/classic",
    2: "https://loldle.net/classic",
    3: "https://narutodle.net/classic",
    4: "https://onepiecedle.net/classic",
    5: "https://pokedle.net/classic",
    6: "https://smashdle.net/classic",
}


def _get_selected_urls(raw_ids):
    if not raw_ids:
        return list(URLS_BY_ID.values())

    selected_urls = []
    for raw_id in raw_ids:
        try:
            url_id = int(raw_id)
        except ValueError:
            continue

        url = URLS_BY_ID.get(url_id)
        if url and url not in selected_urls:
            selected_urls.append(url)

    return selected_urls


def run(selected_ids=None):
    url_list = _get_selected_urls(selected_ids or [])

    if not url_list:
        print("No valid URL IDs were provided. Nothing to run.")
        return

    print(f"Running {len(url_list)} URL(s)...")

    for url in url_list:
        write_database(url)
        options, driver, wait = newDriver(url, headless=False)
        get_solution(options, driver, wait, url)
        driver.quit()


run(sys.argv[1:])