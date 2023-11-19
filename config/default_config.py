DEFAULT_CONFIG = {
    'grafana': {
        'url': 'http://localhost:3000',
        'api_key': '',
        'user': 'admin',
        'password': 'admin'
    },
    'ansible': {
        'inventory_path': './ansible/inventory/hosts.ini',
        'playbook_path': './ansible/playbooks'
    },
    'data': {
        'dashboards_dir': './data/downloads',
        'export_dir': './data/exports'
    },
    'logging': {
        'log_file': 'automons.log',
        'log_level': 'INFO'
    }
}
