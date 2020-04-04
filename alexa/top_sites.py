import requests
from bs4 import BeautifulSoup


class TopSites:
    weights = {}

    def __init__(self):
        self.url = "https://www.alexa.com/topsites/category/Top/Business/Investing"

    def collect(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        for site_listing in soup.find_all("div", {"class": "site-listing"}):
            # Site column
            site_link = site_listing.find("div", {"class": "DescriptionCell"}).find("a")
            cols = site_listing.find_all("div", {"class": "right"})
            # Daily time on site
            daily_time = cols[0].find("p")
            # Daily page views per visitor
            daily_pageviews = cols[1].find("p")
            # % of traffic from search
            traffic_percentage = cols[2].find("p")
            # Total sites linking in
            total_sites_linking = cols[3].find("p")
            print("----")
            print("Website: %s" % (site_link.text))
            print("Daily page views per visitor: %s" % (daily_pageviews.text))
            print("Percentage of traffic from search: %s" % (traffic_percentage.text))
            print("Total sites linking in: %s" % (total_sites_linking.text))
            TopSites.weights[site_link.text.lower()] = int(total_sites_linking.text.replace(',', ''))
            print()
