# ansible_manager.py
import os
from jinja2 import Environment, FileSystemLoader
import yaml

from templates.template_manager import TemplateManager


class AnsibleManager:
    def __init__(self, templates_dir, output_dir):
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        self.output_dir = output_dir

    class AnsibleManager(TemplateManager):
        def add_task_to_playbook(self, task_definition, playbook_name):
            # Load the existing playbook if it exists
            playbook_path = os.path.join(self.output_dir, f'{playbook_name}.yml')
            if os.path.exists(playbook_path):
                playbook_data = self.load_yaml(playbook_path)
            else:
                playbook_data = []

            # Add the new task to the playbook data
            playbook_data.append(task_definition)

            # Save the updated playbook data back to the file
            self.save_yaml(playbook_data, f'{playbook_name}.yml')

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def create_playbook(self, playbook_name, tasks):
        playbook_path = os.path.join(self.output_dir, f'{playbook_name}.yml')
        with open(playbook_path, 'w') as file:
            yaml.dump(tasks, file, default_flow_style=False)
        print(f"Playbook created at {playbook_path}")

    def generate_task(self, task_template, context={}):
        return yaml.safe_load(self.render_template(task_template, context))

    def build_playbook(self, playbook_name, task_templates, context={}):
        tasks = [self.generate_task(task_template, context) for task_template in task_templates]
        self.create_playbook(playbook_name, tasks)


# Usage example
templates_dir = 'path/to/ansible_templates'
output_dir = 'path/to/ansible_output'
ansible_manager = AnsibleManager(templates_dir, output_dir)

task_templates = [
    'checks/check_docker.yml.j2',
    'checks/check_health.yaml.j2.yml.j2',
    'checks/check_status.yml.j2',
    'tasks/install_docker.yml.j2',
    'tasks/run_docker.yml.j2',
    'tasks/update_system.yml.j2',
    'tasks/stop_docker.yml.j2',
    'tasks/export_template.yml.j2'
]

ansible_manager.build_playbook('site', task_templates)
