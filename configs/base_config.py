from os import path


PROJECT_NAME: str = ""


DEV: bool = False

TRACKBACK: bool = True


# """Config Directory of config file"""
CONFIG_DIRECTORY: str = path.dirname(path.realpath(__file__))

# """Root Directory In Service Running"""
APPLICATION_ROOT: str = path.realpath(os.path.join(CONFIG_DIRECTORY, '..'))
PROJECT_NAME = PROJECT_NAME or path.basename(path.realpath(APPLICATION_ROOT))


LOG_FILECONFIG_EXT:str = 'yml' 
LOG_FILECONFIG:str = path.join(CONFIG_DIRECTORY, f'logging.{LOG_FILECONFIG_EXT}')
# Create Log file name in {BASE_PATH}/logs/*.log
LOG_NAME:str = ""
LOG_FILENAME:str = path.join(APPLICATION_ROOT, 'logs', LOG_NAME or f"{PROJECT_NAME}.log")



# Create directory if not exist.
DIRECTORY_INIT: list= [LOG_FILENAME]


DB_URI:str = ""


