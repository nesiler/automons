import json
import os

from default_config import DEFAULT_CONFIG


class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_config(self, config_data):
        with open(self.config_file, 'w') as file:
            json.dump(config_data, file, indent=4)

    def get_config(self):
        return self.config_data

    def update_config(self, section, key, value):
        if section in self.config_data and key in self.config_data[section]:
            self.config_data[section][key] = value
            self.save_config(self.config_data)
        else:
            raise ValueError("Invalid section or key in configuration.")

    def reset_to_defaults(self):
        self.save_config(DEFAULT_CONFIG)
        self.config_data = DEFAULT_CONFIG


# Main for test
if __name__ == "__main__":
    cm = ConfigManager()
    print("Current config:", cm.get_config())
    # Example usage: cm.update_config('grafana', 'url', 'http://new.grafana.server:3000')
    # cm.reset_to_defaults()
