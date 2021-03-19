import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser

def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()
def main():
    url = 'https://www.skysports.com/premier-league-table'
    xhtml = url_get_contents(url).decode('utf-8')

    #using html parser 
    p = HTMLTableParser()
    p.feed(xhtml)
    pprint(p.tables)

    #using beutifulsoup

    #soup=Beutifulsoup(f.text,)

if __name__ == '__main__':
    main()