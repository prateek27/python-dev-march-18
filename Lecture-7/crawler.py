import requests
from bs4 import BeautifulSoup

def get_links(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html5lib")
	links = soup.findAll('a')
	urls = [link['href'] for link in links if link.has_attr('href') and link['href'].startswith('http')]
	return urls


def spider(url, limit=100):
	pagesToVisit = [url]
	pagesVisited = []

	while len(pagesVisited) < limit and pagesToVisit != []:
		url = pagesToVisit.pop(0)
		pagesVisited.append(url)

		print("Visiting " + url)
		new_links = get_links(url)
		for link in new_links:
			if link not in pagesVisited and link not in pagesToVisit:
				pagesToVisit.append(link)

if __name__ == "__main__":
	spider("https://indianpythonista.wordpress.com")