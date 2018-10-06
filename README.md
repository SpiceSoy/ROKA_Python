# ROKA_Python
Python Folder in R.O.K.A

현재 A* 연습기 작업 진행상황:

노드 아닌 영역(검은색 영역)에 대한 예외처리 버그 - 현재 -1,-1의 오브젝트에 클릭처리됨
canvasUtill.py 의 checkClickedIndex 단에서 창의 클릭 좌표 -> 노드 좌표 (인덱스) 로 변환해주는데
여기서 유효검사 하면서 -1 -1 이 되고 -1 -1 의 인덱스에 접근해서 클릭처리됨

참고자료 :
1) https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
