# Automatic Monitoring System (automons)

### Technologies:

- Grafana
- Docker
- Python
- Jinja2
- Ansible

### Project Overview:

Automons is designed to facilitate the seamless deployment and management of Grafana dashboards on remote hosts using
Docker, Python, Jinja2, and Ansible. The system allows users to configure various parameters through a command-line
interface, enabling the creation and maintenance of Grafana dashboards effortlessly.

### Key Features:

1. **Command Line Interface:**
    - The system operates through a command-line interface.
    - Users can input various parameters to specify the target host and desired dashboard configurations.

2. **Docker-Compose for Dashboard Deployment:**
    - Utilizes Docker-Compose to deploy the desired dashboard on the specified host.
    - Jinja2 templates are employed for Docker-Compose, Ansible, and Grafana configurations, providing flexibility and
      customization options.

3. **Ansible for Remote Host Management:**
    - Implements Ansible for the management of remote hosts, streamlining the deployment process.

4. **Grafana Labs Integration:**
    - Users have the option to download dashboards from Grafana Labs using the dashboard ID.
    - The program ensures correct configuration and file integrity checks before installation on the remote host.

5. **Template Folder Support:**
    - Users can utilize a template folder for storing configuration files and the Docker-Compose file.
    - The program validates and corrects all files within the template folder, ensuring seamless deployment.
    - User also have the option to export the current configuration files to a template folder for future use.

6. **Dashboard Deletion Option:**
    - Provides the option for users to delete dashboards from remote hosts, offering flexibility in managing deployed
      dashboards.

7. **Template Folder Creation:**
    - Users can leverage the program to create a template folder for the dashboard and configuration files, enhancing
      organization and reusability.

8. **Datasource Management:**
    - Users have the option to create datasources and install them on hosts without deploying Grafana dashboards.

9. **Included Exporters:**
    - Users can choose from a list of included exporters to install on the remote host.

10. **Supported Distributions and Plugins:**
    - Compatible with Debian-based distributions (e.g., Ubuntu, Debian).
    - Supported datasources and plugins include Prometheus and related plugins.

11. **Compatibility Checks:**
    - The program supports only a select number of datasources and plugins, ensuring compatibility and reliability.
    - Dashboards older than three years (last update) are not supported to prevent potential compatibility issues.

## Parameters and Features

- **--help:** Provides information about parameters and their usage.

- **-d, --dashboard:** Dashboard ID(s) from Grafana Labs.
    - This command allows specifying one or more dashboard IDs for download from Grafana Labs.
    - Example:
      ```sh
      automons -d 1860
      ```
      This downloads the dashboard from "https://grafana.com/api/dashboards/1860," including necessary data sources and
      plugins, and then configures and installs them.

- **--host:** Host or hosts to install.
    - Examples:
        1. If no host is entered, it will be uploaded to the discovered system.
        ```sh
        automons -d 1860
        ```
        2. If a word is given as input, it serves as the host group name for Ansible.
        ```sh
        automons -d 1860 --host test
        ```
        3. If an IP is entered as input, only that IP address will be set up.
        ```sh
        automons -d 1860 --host 192.168.1.5
        ```

- **-t, --temp:** Path of the template folder to install.
    - This parameter takes the path to a folder and file structure previously defined and created by the software. It
      installs to the files in this path.
    - Example:
      ```sh
      automons -t /home/me/my-template --host test
      ```
      (The template structure is specified below.)

- **-e, --export:** Path to export the configuration.
    - This parameter exports the current configuration to the files in this path.

- **--port:** Port to be used.
    - This parameter specifies the port for the dashboard. If not specified, the default port is used.
    - Example:
      ```sh
      automons -d 1860 --port 3000
      ```

- **--only-create:** Creates the template folder for the dashboard and configuration files.

- **--only-send:** Sends the configuration files to the remote host.

- **--only-datasource:** Installs only the datasource and plugins, excluding Grafana.
 
- **--delete:** Deletes the dashboard from the remote host. 

- **-u, --user:** Username for the dashboard.

- **-p, --password:** Password for the dashboard (same as user).

- **--version:** Displays version information of the program.

## Template Structure

The template structure is as follows:

```sh
template
|-- ansible
|   |-- playbook.yml
|-- conf
|   |-- grafana.ini
|-- datasources
|   |-- datasource.yaml
|-- dashboards
|   |-- dashboard.yaml
|-- library
|   |-- dashboard.json
|-- plugins
|    |-- plugins.txt
|-- docker-compose.yml
```

### Example:

```sh
automons -d 1860 --host test --port 3000 --user admin --pass --force
```

#### Output

All steps are indicated with line of characters.
We can use '#' for summary, '*' for information, '-' for warning, '!' for error, '=' for success, '>' for inputs and '+'
for generated files.

```sh
############################################
DASHBOARD ID: 1860
HOST_GROUP: test
PORT: 3000
STATE: install
USER: admin
PASS: DEFAULT or NOT
FORCE: True
############################################

********************************************
Getting data from grafana labs...
Checking if the dashboard exists...
Checking if the dashboard is deprecated...
Checking if the dashboard\'s datasource is supported...
Checking the checking of checkings...
********************************************

############################################
DASHBOARD NAME: Node Exporter Full
DASHBOARD ID: 1860
DASHBOARD URL: https://grafana.com/api/dashboards/1860
DASHBOARD VERSION: 1.0.0
DASHBOARD LAST UPDATED: 2020-04-30T14:00:00Z
DASHBOARD DATASOURCE: Prometheus
DASHBOARD PLUGINS: grafana-piechart-panel, grafana-worldmap-panel
############################################

++++++++++++++++++++++++++++++++++++++++++++
Downloading dashboard : grafana.com/api/dashboards/1860
Dashboard downloaded.
++++++++++++++++++++++++++++++++++++++++++++

--------------------------------------------
>Please select the exporters you want to use:
1. Node Exporter [ default ]
2. Cadvisor [ ]
3. Blackbox Exporter [ ]
--------------------------------------------

--------------------------------------------
WARNING: The following files exist in the path. If you continue, they will be overwritten.
--------------------------------------------

++++++++++++++++++++++++++++++++++++++++++++
Creating configuration files to /etc/automons/templates/1860_node_prometheus
Dashboard configuration file created:
/etc/automons/templates/1860_node_prometheus/dashboards/dashboard.yaml
Datasource configuration file created:
/etc/automons/templates/1860_node_prometheus/datasources/datasource.yaml
Creating docker-compose file:
/etc/automons/templates/1860_node_prometheus/docker-compose.yml
Creating ansible playbook:
/etc/automons/templates/1860_node_prometheus/ansible/playbook/playbook.yml
++++++++++++++++++++++++++++++++++++++++++++

--------------------------------------------
Autobots checking the system...
--------------------------------------------

********************************************
Check if ansible is installed...
Check if hosts are reachable...
Check if hosts are updated...
Check if docker is installed...
Check if docker-compose is installed...
Another check for the sake of Cybertron...
********************************************

--------------------------------------------
No decepticons found. System ready.
--------------------------------------------

********************************************
Running docker-compose...
... docker outputs ...
... docker outputs ...
... docker outputs ...
...ansible outputs...
...ansible outputs...
Well, well, well. Look who\'s here at: http://localhost:3000
********************************************

============================================
SUCCESS: Dashboard is up and running.
PORT: 3000
HOST_GROUP: test
WORLD: Safe for now.
============================================
```

### THE PROJECT STRUCTURE

```sh
automons/
│
├── automons.py             # Main script to run the CLI tool
│
├── cli/
│   ├── cli_parser.py       # Module to handle CLI arguments and options
│   └── commands.py         # Definitions of CLI commands and their actions
│
├── config/
│   ├── default_config.py   # Default configurations for the tool
│   └── config_manager.py   # Module to manage configurations (read/write)
│
├── templates/              # Jinja2 templates for various configurations
│   ├── ansible/
│   │   ├── playbook.yaml.j2
│   │   ├── inventory.yaml.j2
│   │   ├── ansible.cfg.j2
│   ├── docker-compose/
│   │   ├── docker-compose.yaml.j2
│   │   ├── grafana.yaml.j2
│   │   ├── prometheus.yaml.j2
│   │   ├── node-exporter.yaml.j2
│   │   ├── cadvisor.yaml.j2
│   │   ├── blackbox-exporter.yaml.j2
│   ├── grafana/
│   │   ├── dashboard.ini.j2
│   │   ├── datasource.ini.j2
│   |   └── grafana.ini.j2
│   ├── datasource/
│   │   ├── datasource.yaml.j2
│   │   └── prometheus.yaml.j2
│   └── dashboard/
│       ├── dashboard.yaml.j2
│
├── ansible/
│   ├── ansible_manager.py  # Module to manage Ansible playbooks and inventory
│   └── inventory/          # Ansible inventory files
│       └── hosts.ini
│
├── docker/
│   ├── docker_manager.py   # Module to manage Docker and Docker-Compose
│   └── dockerfiles/        # Dockerfiles if needed for custom images
│
├── grafana/
│   ├── dashboard_manager.py  # Module to manage Grafana dashboards
│   └── grafana_api.py        # Module to interact with Grafana API
│
├── utils/
│   ├── scraper.py          # Utility to scrape data from Grafana Labs
│   └── helpers.py          # General utility functions
│
├── tests/                  # Unit tests for the application
│   ├── test_cli_parser.py
│   ├── test_config_manager.py
│   ├── test_ansible_manager.py
│   ├── test_docker_manager.py
│   └── test_dashboard_manager.py
│
├── .env                    # Environment variables for sensitive information
├── requirements.txt        # Python dependencies to be installed
├── Dockerfile              # Dockerfile to containerize the tool if needed
├── docker-compose.yml      # Docker-Compose file to run the tool in containers
└── README.md               # Documentation on how to use the tool
```