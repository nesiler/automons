# template_manager.py
import os
import yaml
from jinja2 import Environment, FileSystemLoader
from docker.docker_manager import DockerManager
from ansible.ansible_manager import AnsibleManager

# Template Manager class
# Created templates structure:
# template
# |-- ansible
# |   |-- playbook.yml
# |-- conf
# |   |-- grafana.ini
# |-- datasources
# |   |-- datasource.yaml
# |-- dashboards
# |   |-- dashboard.yaml
# |-- library
# |   |-- dashboard.json
# |-- docker-compose.yml

class TemplateManager:
    def __init__(self, template_dir, output_dir, services_dir):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.output_dir = "../data/exports"
        self.services_dir = services_dir

    def create_template(self, template_name):
        # Define the directory structure
        directories = [
            'ansible',
            'conf',
            'datasources',
            'dashboards',
            'library'
        ]

        base_path = os.path.join(self.output_dir, template_name)
        os.makedirs(base_path, exist_ok=True)

        # Create the subdirectories
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)

        # Create the docker-compose.yml file
        docker_manager = DockerManager('templates/docker', base_path)



    def load_service_definition(self, service_name):
        service_file = f'{self.services_dir}/{service_name}.yaml'
        with open(service_file, 'r') as file:
            return yaml.safe_load(file)

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def write_output(self, file_name, content):
        output_path = os.path.join(self.output_dir, file_name)
        with open(output_path, 'w') as file:
            file.write(content)
        print(f"File created at {output_path}")

    def load_yaml(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def save_yaml(self, data, file_name):
        output_path = os.path.join(self.output_dir, file_name)
        with open(output_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print(f"YAML file saved at {output_path}")
