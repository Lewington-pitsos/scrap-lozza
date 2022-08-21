import requests
from bs4 import BeautifulSoup

def get_html_for_url(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def get_podcast_links(html):
    links = []
    for link_holder in html.find_all('ul', {"class": "libsyn-item-free"}):
        link = link_holder.find('a')
        if link.has_attr('href'):
            links.append(link['href'])
    return links

url = "https://wttpodcast.libsyn.com/page/1/size/100"
html = get_html_for_url(url)
links = get_podcast_links(html)
print(links)