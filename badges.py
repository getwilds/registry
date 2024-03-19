from ghapi.all import GhApi
import base64
import markdown
from bs4 import BeautifulSoup

ORG = 'getwilds'
api = GhApi()

def extract_badges(repo):
	try:
		x = api.repos.get_content(ORG, repo, "README.md")
	except Exception as e:
		return []

	readme = base64.b64decode(x['content']).decode('utf-8')
	readme_html = markdown.markdown(readme)
	soup = BeautifulSoup(readme_html, "html.parser")
	badges = []
	for a in soup.find_all('a'):
		if any([w.name == "img" for w in a.children]):
			badges.append(a.attrs | a.img.attrs)
	return badges
