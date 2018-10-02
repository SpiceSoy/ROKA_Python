from tkinter import *
from RectClass import *
from canvasUtill import *

#메인 윈도우 생성
mainWindow = Tk()
mainWindow.title("알고리즘 공부합시다!")
mainWindow.geometry("1100x783+50+15")
mainWindow.resizable(False,False)

#캔버스 생성
drawCanvas = Canvas(mainWindow,width=780,height=780)
drawCanvas.pack(side=LEFT)
drawCanvas.configure(background='black')

#세팅값 설정
canvasRectSetting = CanvasRectSetting(15,15,30,25)
class State:
    def __init__(self,state):
        self.state = state
editMode = State(False)

#Rect생성
rectList = list()
for yCount in range(canvasRectSetting.rectMax):
    tempYlist = list()
    for xCount in range(canvasRectSetting.rectMax): 
        tempYlist.append(Rect(drawCanvas,rectList,xCount,yCount,canvasRectSetting,'white'))
    rectList.append(tempYlist)


#툴 프레임 생성
toolFrame = Frame(mainWindow,background='black')
toolFrame.pack(fill='both',side=LEFT,ipadx=400)

#제목 라벨 생성
labelText = Label(toolFrame,text="A* 알고리즘 테스트기")
labelText.pack(fill='x')

#디버그 라벨 생성
clickDebugText = Label(toolFrame,text="클릭 테스트")
clickDebugText.pack(fill='x')


#캔버스 클릭 지정
def canavsClicked(event):
    temp = calcIndex(event.x,event.y,canvasRectSetting)
    
    clickDebugText.configure(
        text = str(event.x) + " , " + str(event.y) + " 위치 클릭 \n " 
        + str(temp[0]) +" , " + str(temp[1]) + "위치의 사각형 클릭" )
    if editMode.state:
         if checkIndex(temp):
            rectList[temp[1]][temp[0]].isClicked(event)
            rectList[temp[1]][temp[0]].Refresh()

drawCanvas.bind("<Button-1>",canavsClicked)

#스타트 버튼 생성
startButton = Button(toolFrame,text="시작")
startButton.pack(fill='x')

#모드 체인지 버튼 생성
modeButton = Button(toolFrame,text="벽 편집하기")
modeButton.pack(fill='x')
def modeChange():
    if editMode.state == False:
        modeButton.configure(text = "벽 편집 종료")
        editMode.state = True
    else:
        modeButton.configure(text = "벽 편집하기")
        editMode.state = False
modeButton.configure(command=modeChange)


#리셋버튼 지정
resetButton = Button(toolFrame,text = "리셋")
resetButton.pack(fill='x')
def reset():
    for ylist in rectList:
        for rectObj in ylist:
            rectObj.color = 'white'
            rectObj.Refresh()
resetButton.configure(command=reset)

#프로그램 UI 루프 시작
mainWindow.mainloop()