# base.py
import requests
from bs4 import BeautifulSoup

def GetRuliWebPS4(page):
    # HTTP GET Request
    req = requests.get('http://bbs.ruliweb.com/ps/board/300001/list?page=' + str(page))
    # HTML 소스 가져오기
    html = req.text

    # html 을 파이썬 객체로 변환

    soup = BeautifulSoup(html,'html.parser')

    my_titles = soup.select(
        'tr.table_body > td > div > a'
    )

    # my_titles는 list 객체
    for title in my_titles:
        # Tag안의 텍스트 , 속성 가져오기
        print(title.text + " : " + title.get('href'))
    return None

pageNum = input("따올 페이지를 선택하세요 : ")
for i in range(1,int(pageNum)):
    GetRuliWebPS4(int(i))