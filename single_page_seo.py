from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import requests

class SiteMap:
    def __init__(self,address):
        self.address = address
        r = urllib.request.urlopen(self.address)
        self.soup = BeautifulSoup(r, 'html.parser')

    def get_site_map(self):
        try:
            xml_url = self.address + '/sitemap.xml'
            open_url = urlopen(xml_url)
            print(open_url)
        except:
            print("there is not sitemap in this URL")

    def get_h_tag(self):
        r = urllib.request.urlopen(self.address)
        headers = self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])
        print([header.get_text() for header in headers])

    def get_canonical_tag(self):

        can = self.soup.find_all('link', attrs={'rel': 'canonical'})
        for q in can:
            print(q['href'])

    def get_robots_txt(self):
        response = requests.get(self.address + "/robots.txt")
        if response:
            print("yourr file is avlinad")
        else:
            print("nott file..")

    def get_img_info(self):
        img_tags = self.soup.find_all('img')
        # print(img_tags['src'])

        for im in img_tags:
            url_im = self.address + "/" + im['src']
            try:
                img_find = urlopen(url_im)
                print(im['alt'])
                print(im['src'])
            except(KeyError):
                print("alt is  not ..")
                print(im['src'])
            except:
                print(im['alt'])
                print(im['src'])

            print("--------------------------------------")

    def get_web_desc(self):
        r = urllib.request.urlopen(self.address)
        soup = BeautifulSoup(r, 'html.parser')
        meta = soup.find_all('meta', attrs={'name': 'description'})

        for tag in meta:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
                print('NAME    :', tag.attrs['name'].lower())
                print('CONTENT :', tag.attrs['content'])

# tt = SiteMap('https://www.wscubetech.com')
tt = SiteMap('https://www.wscubetech.com/login.html')

print("hading tag...")
tt.get_h_tag()
print("canonical tag...")
tt.get_canonical_tag()
print("robots txt")
tt.get_robots_txt()
print("img.........")
tt.get_img_info()
print("desc............")
tt.get_web_desc()