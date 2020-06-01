#!/bin/sh

chmod +x __main__.py

echo "Python version."
python3 -V

echo "which python3"
which python3

if [ ! -d "venv/" ] 
then
    echo "Create Python Virtual Envelopment." 
    python3 -m virtualenv venv
else
    echo "Python Virtual Envelopment is exist."
fi

echo "Init python virtual envelopment"
source venv/bin/activate

if [ ! -f "venv/bin/py" ] 
then
    echo "alise python3 => py"
    cp "$(which python3)" venv/bin/py
fi
which py

if [ -f "requirements.txt" ] 
then
    echo "Install Python Module." 
    python3 -m pip install -U pip
    python3 -m pip install -r requirements.txt
else
    echo "No file requirements.txt"
fi

if [ ! -f ./configs/config.py ] 
then
    echo "" > configs/config.py
fi

python3 -m pip install pyyaml

echo "Init end."
