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

def download_links(links):
    for link in links:
        name = link.split('/')[-1]
        doc = requests.get(link)
        with open(name, 'wb') as f:
            f.write(doc.content)
            print(f"Saved {name}")

def generate_urls(n_pages, results_per_page):
    urls = []
    for i in range(1, n_pages+1):
        urls.append(f"https://wttpodcast.libsyn.com/page/{i}/size/{results_per_page}")
    return urls

def main():
    urls = generate_urls(13, 25)
    for i, url in enumerate(urls):
        print("downloading all podcasts on page", i + 1)
        html = get_html_for_url(url)
        links = get_podcast_links(html)
        download_links(links)

main()