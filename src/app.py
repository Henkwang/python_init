# system import
import os
import logging, logging.config
import yaml


# import config
from configs import base_config as pyConfig



def create_app(dict_config: dict = None, *, pyfile=None) -> bool:

    update_more_pyConfig(pyfile)

    update_config_enverlopment()

    update_config_dict(dict_config)

    create_directory()

    set_loging_from_config()

    print_configs()

    #todo run service
    logging.info('Running...')

    return True


"""
───────────────────────────────────────
                                       
O┬  ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔     O┬         
┌┘  ╠╣ ║ ║║║║║   ║ ║║ ║║║║     ┌┘         
┴O  ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝     ┴O         
O┬  ╔═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╦╔═╗╔╗╔  O┬      
┌┘  ║ ║╠═╝║╣ ╠╦╝╠═╣ ║ ║║ ║║║║  ┌┘      
┴O  ╚═╝╩  ╚═╝╩╚═╩ ╩ ╩ ╩╚═╝╝╚╝  ┴O      
                                       
───────────────────────────────────────                                                                                    
"""
def set_loging_from_config():
    check_attr = hasattr(pyConfig, 'LOG_FILECONFIG_EXT')
    check_log_file_config_is_exist = hasattr(pyConfig, 'LOG_FILECONFIG') and os.path.isfile(pyConfig.LOG_FILECONFIG)
    if  check_attr and check_log_file_config_is_exist:
        if pyConfig.LOG_FILECONFIG_EXT.lower() in ['yml', 'yaml']:
            with open(pyConfig.LOG_FILECONFIG, 'r') as f:
                fr = f.read()
                fr = fr.format(LOG_FILENAME=pyConfig.LOG_FILENAME)
                log_cfg = yaml.safe_load(fr)
                # print(log_cfg)
                logging.config.dictConfig(log_cfg)
        elif pyConfig.LOG_FILECONFIG_EXT.lower() in ['ini']:
            logging.config.fileConfig(pyConfig.LOG_FILECONFIG)
        else:
            raise Exception("python logfile config not support.")
    if not check_log_file_config_is_exist:
        raise FileNotFoundError('file config log error: %s', pyConfig.LOG_FILECONFIG)


def update_more_pyConfig(more_pyConfig = None):
    if more_pyConfig:
        list_more_configs = [item for item in dir(more_pyConfig) if item.isupper() and not item.startswith("__")]
        for name_config in list_more_configs: 
            if hasattr(pyConfig, name_config):
                setattr(pyConfig, name_config, getattr(more_pyConfig, name_config))



def update_config_dict(dictConfig: dict):
    if dictConfig and len(dictConfig) > 0:
        for key, val in dictConfig.items():
            try:
                setattr(pyConfig, key.upper(), val)
            except Exception as ex:
                logging.warning(f'Not set config {key}:{val}, Exception: {ex}')


def update_config_enverlopment(prefix: str = None):
    if not prefix or len(prefix) == 0:
        prefix = None
    list_name_configs = [item for item in dir(pyConfig) if item.isupper() and not item.startswith("__")]
    for name_config in list_name_configs:
        if prefix:
            name_env = f'{prefix}_{name_config}'
        else:
            name_env = name_config

        val_env = os.getenv(name_env)
        if val_env:
            try:
                if isinstance(getattr(pyConfig, name_config), list):
                    if isinstance(val_env, str):
                        val_env = val_env.split(',')

                setattr(pyConfig, name_config, val_env)

            except Exception as ex:
                logging.warning(f'Not set config {name_env}:{val_env}, Exception: {ex}')


def create_directory():
    if hasattr(pyConfig, 'DIRECTORY_INIT') and isinstance( pyConfig.DIRECTORY_INIT, list):
        for d in pyConfig.DIRECTORY_INIT:
            print("Init Directory:", d)
            os.makedirs(d, exist_ok=True)

def print_configs():
    list_name_configs = [item for item in dir(pyConfig) if item.isupper() and not item.startswith("__")]
    for name_config in list_name_configs:
        logging.debug('Config => %s: %s', name_config, getattr(pyConfig, name_config))
        # print('Config => %s: %s' % ( name_config, getattr(pyConfig, name_config)))


def run_testing():
    pass
