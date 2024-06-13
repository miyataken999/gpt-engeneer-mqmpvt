import requests
from bs4 import BeautifulSoup
from .models import Website, Page
from .database import db_session

class Crawler:
    def __init__(self, start_url):
        self.start_url = start_url
        self.visited = set()

    def crawl(self):
        self._crawl(self.start_url)

    def _crawl(self, url):
        if url in self.visited:
            return
        self.visited.add(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pages = [a['href'] for a in soup.find_all('a', href=True)]
        for page in pages:
            self._crawl(page)
        website = Website(url=url)
        db_session.add(website)
        db_session.commit()
        for page in pages:
            page_obj = Page(url=page, website_id=website.id)
            db_session.add(page_obj)
        db_session.commit()