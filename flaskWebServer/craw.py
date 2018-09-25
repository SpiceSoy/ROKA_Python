import requests
from bs4 import BeautifulSoup

def GetRuliNews(page):
    # HTTP GET Request
    req = requests.get('https://bbs.ruliweb.com/news?&page='+ str(page))
    # HTML 소스 가져오기
    html = req.text

    # html 을 파이썬 객체로 변환

    soup = BeautifulSoup(html,'html.parser')
    my_article = list()
    my_article = soup.select('ul.row > li')
    # # my_titles는 list 객체
    # for title in my_titles:
    #     # Tag안의 텍스트 , 속성 가져오기
    #     print(title.text + " : " + title.get('href'))
    return my_article
    #vContent > div:nth-child(5) > font:nth-child(1) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(9) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)