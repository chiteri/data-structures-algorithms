import sys
import urllib 
import re
from urlparse import urlparse

class BarebonesCrawler:
    def __init__(self):
        self.queue = [] # Websites to crawl
        self.discovered = set() # URLs of discovered websites

    def discover(self, root):
        self.queue.append(root)
        self.discovered.add(root)

        while len(self.queue) > 0:
            visited = self.queue.pop()
            print visited 

            # Read in raw html from the next website in queue
            webpage = urllib.urlopen(visited)
            content = webpage.read()

            # Use regular expression to find all URLs in website of 
            # form http(s)://www.yyy.zzz (Crude, misses relative URLs)
            results = re.findall(r'(https?://[^\s]+)', content)

            while len(results) > 0:
                output = urlparse(results.pop())
                link = output.scheme + '://' + output.hostname 

                # if not discovered mark it as discovered and place it on the queue 
                if link not in self.discovered:
                    self.discovered.add(link)
                    self.queue.append(link)


if __name__ == "__main__":
    address = str(sys.argv[1]).lower() # Pass a URL such as http://www.w3.org
    web_crawler = BarebonesCrawler()
    web_crawler.discover(address)
