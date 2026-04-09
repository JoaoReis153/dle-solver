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

echo "Select URLs by ID (space-separated):"
echo "1 - https://dotadle.net/classic"
echo "2 - https://loldle.net/classic"
echo "3 - https://narutodle.net/classic"
echo "4 - https://onepiecedle.net/classic"
echo "5 - https://pokedle.net/classic"
echo "6 - https://smashdle.net/classic"
echo

if [ -t 0 ]; then
    read -r -p "IDs (example: 1 2 4): " raw_ids
elif [ -r /dev/tty ]; then
    read -r -p "IDs (example: 1 2 4): " raw_ids < /dev/tty
else
    raw_ids=""
fi

valid_ids=()
for raw_id in $raw_ids; do
    if [[ "$raw_id" =~ ^[1-6]$ ]]; then
        valid_ids+=("$raw_id")
    fi
done

if [ ${#valid_ids[@]} -eq 0 ]; then
    echo "No valid IDs provided, running all URLs."
    python3 ./main.py
else
    echo "Running IDs: ${valid_ids[*]}"
    python3 ./main.py "${valid_ids[@]}"
fi