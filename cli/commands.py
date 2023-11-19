import utils.scraper as scraper
import models.dashboard as Dashboard
import templates.template_manager as tm
import docker.docker_manager as docker_manager

scraper = scraper.DashboardScraper()
tm = tm.TemplateManager()

def download_dashboard(dashboard_id):
    return scraper.scrape_dashboard_data(dashboard_id)


def create_template_folder(dashboard_id, port, user, password, datasource_only):
    dashboard = Dashboard(dashboard_id, port, user, password, datasource_only)

    # download the dashboard
    # then create the template folder



def install_dashboard_from_lab(host, dashboard_id, port, user, password, datasource_only):
    #     print all the parameters for debugging in one print
    print(
        f"Destination: {host}\nDashboard ID: {dashboard_id}\nPort: {port}\nUser: {user}\nPassword: {password}\nDatasource Only: {datasource_only}")


def install_dashboard_from_template(host, template_path, port, user, password, datasource_only):
    print(
        f"Destination: {host}\nTemplate Path: {template_path}\nPort: {port}\nUser: {user}\nPassword: {password}\nDatasource Only: {datasource_only}")


def delete_dashboard(host_group, port, user, password, datasource_only):
    # print all the parameters for debugging in one print
    print(f"Host Group: {host_group}")


def send_configuration_from_lab(host_group, dashboard_id, port, user, password, datasource_only):
    # print all the parameters for debugging in one print
    print(f"Host Group: {host_group}\nTemplate Path: {dashboard_id}")


def send_configuration_from_template(host_group, template_path):
    # print all the parameters for debugging in one print
    print(f"Host Group: {host_group}\nTemplate Path: {template_path}")


def export_configuration(export_path):
    # print all the parameters for debugging in one print
    print(f"Export Path: {export_path}")


# Process Arguments method
def process_arguments(args):
    # If one of the source --dashboard is provided, install the dashboard on the host
    if (args.dashboard is not None
            and args.host is None):
        install_dashboard_from_lab(args.host, args.dashboard, args.port, args.user, args.password, args.only_datasource)

    # If one of the source --temp is provided, install the dashboard on the host
    if (args.temp is not None
            and args.host is None):
        install_dashboard_from_template(args.temp, args.dashboard, args.port, args.user, args.password,
                                        args.only_datasource)

    # if --only-create and dashboard is provided, create the template folder
    if (args.only_create
            and args.dashboard is not None):
        create_template_folder(args.dashboard, args.port, args.user, args.password, args.only_datasource)

    # If --delete and --host are provided, it means we want to delete the dashboard from the host
    if (args.delete
            and args.host is not None):
        delete_dashboard(args.host)

    # If --only-send, --host, and --dashboard are provided, it means we want to send the configuration to the host
    if (args.only_send
            and args.host is not None
            and args.dashboard is not None):
        send_configuration_from_lab(args.host, args.dashboard)

    # If --only-send, --host, and --temp are provided, it means we want to send the configuration to the host
    if (args.only_send
            and args.host is not None
            and args.temp is not None):
        send_configuration_from_template(args.host, args.temp)

    # If only --export is provided
    if (args.export is not None
            and args.host is None
            and args.dashboard is None
            and args.temp is None
            and not args.only_send):
        export_configuration(args.export)
