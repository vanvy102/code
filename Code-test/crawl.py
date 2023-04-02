import requests
from bs4 import BeautifulSoup
#headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
header='https://s.cafef.vn'
URL="https://s.cafef.vn/hose/ACB-ngan-hang-thuong-mai-co-phan-a-chau.chn"
resp=requests.get(url=URL)
soup=BeautifulSoup(resp.content,"html.parser")
link=soup.find('div',attrs={'id':'divTopEvents'})
print(type(link))
crawl_link=link.find_all('a')
print(len(crawl_link))
URLS=[]
for links in crawl_link:
    URLS.append(links['href'])
webs=[]
for u in URLS:
    k=header+ u
    webs.append(k)
print(webs)
#print(webs[1])
#fp=open('check.txt','w',encoding="utf-8")
#fp.write(check)
#fp.close()
