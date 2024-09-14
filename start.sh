#clear console
clear

#create VE
python3 -m venv myenv

#activate VE
source myenv/bin/activate


#install packages
pip install selenium
pip install webdriver_manager

#clear the terminal
clear

#run
#python3 ./main.py
python3 ./utils.py

deactivate

find . -name '__pycache__' -type d -exec rm -r {} +

if [ -d "myenv" ]; then
    rm -rf myenv
fi
