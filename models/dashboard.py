class Dashboard:
    def __init__(self, name, dashboard_id, url, datasource, plugins):
        self.name = name
        self.dashboard_id = dashboard_id
        self.url = url
        self.datasource = datasource

    def __str__(self):
        return (f"Dashboard:\n"
                f"Name: {self.name}\n"
                f"ID: {self.dashboard_id}\n"
                f"URL: {self.url}\n"
                f"Datasource: {self.datasource}\n")


# Example:
node_exporter_dashboard = Dashboard(
    name="Node Exporter Full",
    dashboard_id=1860,
    url="https://grafana.com/api/dashboards/1860",
    datasource="Prometheus"
)

# main for test
if __name__ == "__main__":
    print(node_exporter_dashboard)
