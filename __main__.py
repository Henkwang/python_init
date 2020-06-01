#!./venv/bin/python
from src.app import create_app
from configs import config

if __name__ == "__main__":
    create_app({}, pyfile=config)