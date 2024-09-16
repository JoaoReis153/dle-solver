#clear console
clear

#create VE
python3 -m venv myenv

#activate VE
source myenv/bin/activate

#install packages from requirements.txt
pip install -r requirements.txt

#clear the terminal
clear

#run the program
python3 ./main.py
#python3 ./utils.py

#deactivate and clean up
deactivate

find . -name '__pycache__' -type d -exec rm -r {} +

if [ -d "myenv" ]; then
    rm -rf myenv
fi
