import os
import re

import argparse


def check_args(args, parser):
    # 1.  If there is no parameter provided, display an error message.
    if args.dashboard is None and args.host is None and args.temp is None and args.export is None:
        parser.error("No parameter provided.")
        exit(0)

    # 2.  If the `--host` parameter is specified, but there is no `--dashboard` or `--temp`, display an error.
    if args.host is not None and not (args.dashboard or args.temp):
        parser.error("Host parameter provided, but no dashboard or template path provided.")
        exit(0)

    # 3.  If both `--dashboard` and `--temp` are provided, display an error.
    if args.dashboard is not None and args.temp is not None:
        parser.error("Dashboard ID(s) and template path cannot be provided together.")
        exit(0)

    # 4. If `--state=delete` is specified along with any other parameter except `--host` parameter, display an error.
    if args.delete and (args.dashboard is not None or args.temp is not None or args.export is not None):
        parser.error("Delete state cannot be used with any other parameter except host.")
        exit(0)

    # 5. If `--state` is specified as `create or send` , but there is no `--dashboard` or `--temp`, display an error.
    if (args.only_create or args.only_send or args.only_datasource) and (args.dashboard is None or args.temp is None):
        parser.error("Create, send or datasource provided, but no dashboard or template path provided.")
        exit(0)

    # 7.  If `--export` is specified, make sure that there is no conflicting parameter like `--dashboard`, `--temp`.
    if args.export is not None and (args.dashboard is not None or args.temp is not None):
        parser.error("Export parameter provided, you cannot provide dashboard or template path.")
        exit(0)

    # 13. If `--port` is specified, ensure that it is a valid port number.
    if args.host and not is_valid_port(args.port):
        parser.error("Port must be a valid port number.")
        exit(0)

    # 15. If `--host` is specified, ensure that it is a valid host.
    if args.host and not is_valid_host(args.host):
        parser.error("Host must be a valid host.")
        exit(0)

    # 16. If `--dashboard` is specified, ensure that it is a valid dashboard ID.
    if args.dashboard and not is_valid_dashboard_id(args.dashboard):
        parser.error("Dashboard ID must be a valid dashboard ID.")
        exit(0)

    # 17. If `--temp` is specified, ensure that it is a valid template path.
    if args.temp is not None and not is_valid_template_path(args.temp):
        parser.error("Template path must be a valid template path.")
        exit(0)
    # 18. If `--export` is specified, ensure that it is a valid export path.
    if args.export is not None and not is_valid_export_path(args.export):
        parser.error("Export path must be a valid export path.")
        exit(0)

    return True


def is_valid_dashboard_id(dashboard_id):
    if dashboard_id <= 0:
        print("Dashboard ID must be a positive integer.")
        return False
    return True


def is_valid_ipv4_address(address):
    try:
        match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', address)
        return bool(match) and all(0 <= int(num) < 256 for num in address.rstrip().split('.'))
    except ValueError:
        return False


def is_valid_host(host):
    if host is None:
        return True
    if is_valid_ipv4_address(host):
        return True
    hosts = []

    with open("./ansible/inventory/hosts.ini", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("["):
                hosts.append(line.strip("[]\n"))

    if host not in hosts:
        print(f"Host '{host}' not found in inventory.")
        return False

    return True


def is_valid_template_path(template_path):
    return template_path != "" and os.path.isdir(template_path) and os.path.exists(template_path)


def is_valid_export_path(export_path):
    return export_path != "" and os.path.isdir(export_path) and os.path.exists(export_path)


def is_valid_port(port):
    return 0 <= port <= 65535


def parse_args():
    parser = argparse.ArgumentParser(description="Automatic Monitoring System (Automons) CLI")
    parser.add_argument("-d", "--dashboard", type=int, help="Dashboard ID from Grafana Labs.")
    parser.add_argument("--host", type=str,
                        help="Host group name or ip address. \n Example: '--host test' or '--host 192.168.1.5'")
    parser.add_argument("-t", "--temp", type=str,
                        help="Path of the template folder to install. \n Example: '--temp templates/test'")
    parser.add_argument("-e", "--export", type=str,
                        help="Path to export the configuration. \n Example: '--export /home/user/automons/export'")
    parser.add_argument("--port", type=int, default=3000, help="Port to be used. \n Example: '--port 3000'")
    parser.add_argument("--only-create", action='store_true', default=False,
                        help="Create the template folder for the dashboard and configuration files.")
    parser.add_argument("--only-send", action='store_true', default=False, help="Send the configuration files.")
    parser.add_argument("--delete", action='store_true', default=False,
                        help="Delete the dashboard from the remote host.")
    parser.add_argument("--only-datasource", action='store_true', default=False,
                        help="Install only the datasource and plugins.")
    parser.add_argument("-u", "--user", type=str, default="admin", help="Username for the dashboard.")
    parser.add_argument("-p", "--password", type=str, default="admin", help="Password for the dashboard.")
    parser.add_argument("--version", action='version', version='%(prog)s 1.0',
                        help="Show program's version number and exit.")
    args = parser.parse_args()

    check_args(args, parser)

    return args
