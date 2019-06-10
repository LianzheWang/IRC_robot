import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def youtube_search(x):
    searching_part = urllib.parse.quote(x)
    link = "https://www.youtube.com/results?search_query=" + searching_part
    r = urllib.request.urlopen(link)
    opened_html = r.read()
    bs = BeautifulSoup(opened_html, "html.parser")
    return 'https://www.youtube.com' + bs.find(attrs={'class': 'yt-uix-tile-link'})['href']
    #return 'https://www.youtube.com' + bs.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href']

