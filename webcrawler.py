import re
import requests

class WebCrawler:

    def __init__(self):
        self.discovered_websites = []

    def crawl(self, start_url):

        queue = [start_url]
        self.discovered_websites = [start_url]

    #standard breadth first search

        while queue:

            actual_url = queue.pop(0)
            print(actual_url)

            actual_url_html = self.read_raw_html(actual_url)

            for url in self.get_links_from_html(actual_url_html):
                
                if url not in self.discovered_websites:

                    self.discovered_websites.append(url)
                    queue.append(url)

    def get_links_from_html(self, raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

    def read_raw_html(self, url):

        raw_html = ''

        try:
            raw_html = requests.get(url).text

        except Exception as e:
            pass

        return raw_html

crawler = WebCrawler()
crawler.crawl("https://www.asu.edu")    