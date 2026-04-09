URLS_BY_ID = {
    1: "https://dotadle.net/classic",
    2: "https://loldle.net/classic",
    3: "https://narutodle.net/classic",
    4: "https://onepiecedle.net/classic",
    5: "https://pokedle.net/classic",
    6: "https://smashdle.net/classic",
}


def format_url_list():
    return "\n".join(f"{url_id} - {url}" for url_id, url in URLS_BY_ID.items())


def get_selected_entries(raw_ids):
    if not raw_ids:
        return list(URLS_BY_ID.items())

    selected_entries = []
    seen_ids = set()

    for raw_id in raw_ids:
        try:
            url_id = int(raw_id)
        except ValueError:
            continue

        if url_id in URLS_BY_ID and url_id not in seen_ids:
            seen_ids.add(url_id)
            selected_entries.append((url_id, URLS_BY_ID[url_id]))

    return selected_entries
