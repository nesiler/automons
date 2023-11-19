# scraper.py
import os
import requests
import utils.printer as out


class DashboardScraper:
    def __init__(self):
        self.base_page_url = "https://grafana.com/grafana/dashboards/{}"
        self.base_json_url = "https://grafana.com/api/dashboards/{}"
        self.data_dir = "../data/downloads"

    def is_dashboard_exists(self, id):
        url = self.base_page_url.format(id)
        response = requests.get(url)
        return response.status_code == 200

    def scrape_dashboard_data(self, dashboard_id):
        if self.is_dashboard_exists(dashboard_id):
            print(f"Dashboard {dashboard_id} exists")
            url = self.base_json_url.format(dashboard_id)
            response = requests.get(url)
            if response.status_code == 200:
                dashboard_json = response.json()
                os.makedirs(self.data_dir, exist_ok=True)
                print(f"Saving dashboard {dashboard_id} to {self.data_dir}")
                with open(f"{self.data_dir}/{dashboard_id}.json", "w") as file:
                    file.write(response.text)
            else:
                out.error_message(f"Dashboard {dashboard_id} could not be downloaded!")
                exit(0)
        else:
            out.error_message(f"Dashboard {dashboard_id} does not exist!")
            exit(0)
        return f"{self.data_dir}/{dashboard_id}.json"


# Main for test
if __name__ == "__main__":
    pass
    # dashboard_ids = [1857, 1858, 1859, 1860, 1861, 1862, 1863]
    # scraper = DashboardScraper()
    # dashboards = scraper.scrape_dashboard_data(dashboard_ids)
    # for dashboard in dashboards:
    #     print(dashboard)
