#!/usr/bin/env bash

# clear console
clear

# create VE when missing
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

# activate VE
source myenv/bin/activate

# install packages from requirements.txt
pip install -r requirements.txt

# clear the terminal
clear

echo "Select URLs to load database by ID (space-separated):"
python3 -c "from url_registry import format_url_list; print(format_url_list())"
echo

if [ -t 0 ]; then
    read -r -p "IDs (example: 1 2 4): " raw_ids
elif [ -r /dev/tty ]; then
    read -r -p "IDs (example: 1 2 4): " raw_ids < /dev/tty
else
    raw_ids=""
fi

if [ -z "$raw_ids" ]; then
    echo "No IDs provided, loading all URLs."
    python3 ./load.py
else
    read -r -a selected_ids <<< "$raw_ids"
    echo "Selected IDs: ${selected_ids[*]}"
    python3 ./load.py "${selected_ids[@]}"
fi
