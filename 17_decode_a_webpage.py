#17_decode_a_webpage.py

import requests
from bs4 import BeautifulSoup


url = 'https://nytimes.com'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html)

for story_heading in soup.find_all(class_='story-heading'):
	if story_heading.a:
		print(story_heading.a.text.replace('\n', ' ').strip())
	else:
		print(story_heading.contents[0].strip())
