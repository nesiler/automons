# docker_manager.py
import os
import yaml
from jinja2 import Environment, FileSystemLoader
import templates.template_manager as tm

class DockerManager:
    def __init__(self, templates_dir, output_dir):
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.output_dir = '../data/exports'

    def add_service_to_compose(self, service_definition, service_name):
        # Load the existing docker-compose.yml if it exists
        compose_path = os.path.join(self.output_dir, 'docker-compose.yml')
        if os.path.exists(compose_path):
            compose_data = tm.load_yaml(compose_path)
        else:
            compose_data = {'version': '3', 'services': {}}

        # Add the new service to the compose data
        compose_data['services'][service_name] = service_definition

        # Save the updated compose data back to the file
        self.save_yaml(compose_data, 'docker-compose.yml')

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def create_docker_compose_file(self, services):
        compose_template = self.render_template('docker-compose.yml.j2', {'services': services})
        compose_path = os.path.join(self.output_dir, 'docker-compose.yml')
        with open(compose_path, 'w') as file:
            file.write(compose_template)
        print(f"Docker-Compose file created at {compose_path}")

    def generate_service(self, service_template, context={}):
        return yaml.safe_load(self.render_template(service_template, context))

    def build_docker_compose(self, service_templates, context={}):
        services = {}
        for service_template in service_templates:
            service_name = service_template.split('/')[-1].split('.')[0]
            services[service_name] = self.generate_service(service_template, context)
        self.create_docker_compose_file(services)
