import os
from pathlib import Path


def set_data_save_path():
    pass


def get_data_save_path():
    pass


def get_config_file_path():
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    config_dir = os.path.join(current_dir, 'config')
    return
