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
|-- docker-compose.yml
```