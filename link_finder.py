from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # On calling HTMLParser feed(), this is called when encountering tag <a> in html
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, values) in attrs:
                # Store full url if relative url found
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, values)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
