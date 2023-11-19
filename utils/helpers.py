import os
import yaml
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_dir, log_file, level=logging.INFO, max_size=10485760, backup_count=5):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)
    handler = RotatingFileHandler(log_path, maxBytes=max_size, backupCount=backup_count)
    logging.basicConfig(level=level, handlers=[handler],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger()


def load_yaml(file_path):
    with open(file_path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)


def save_yaml(data, file_path):
    with open(file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file, default_flow_style=False)


def ensure_directory_exists(directory):
    os.makedirs(directory, exist_ok=True)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)