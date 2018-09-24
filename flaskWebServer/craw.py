import requests
from bs4 import BeautifulSoup

def titlesort(obj):
    return obj.text

def GetCommicList(uid):
    # HTTP GET Request
    req = requests.get('https://marumaru.in/?c=1/28&uid=' + str(uid))
    # HTML 소스 가져오기
    html = req.text

    # html 을 파이썬 객체로 변환

    soup = BeautifulSoup(html,'html.parser')
    commicTitle = soup.select_one('.subject > h1')
    my_titles = list()
    my_titles += soup.select('#vContent > div > font > a')
    my_titles += soup.select('#vContent > div > font > span > a')
    my_titles += soup.select('#vContent > div > span > a')
    my_titles += soup.select('#vContent > div > div > font > a')
    my_titles += soup.select('#vContent > div > div > font > span > a')
    my_titles += soup.select('#vContent > div > div > span > a')
    my_titles.sort(key=titlesort)

    
    # # my_titles는 list 객체
    # for title in my_titles:
    #     # Tag안의 텍스트 , 속성 가져오기
    #     print(title.text + " : " + title.get('href'))
    return (commicTitle.text,my_titles)
    #vContent > div:nth-child(5) > font:nth-child(1) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(9) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)
    #vContent > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)