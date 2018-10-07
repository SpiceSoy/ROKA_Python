from tkinter import *
from canvasUtill import *
from EditUtill import *
from naviContainer import *
from RectContainer import *

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
canvasRectSetting = CanvasRectSetting(15,15,30,25,25)
editMode = EditMode(EditState['noneEdit'])

#naviContainer 생성
naviTileContainer = NaviTileContainer(canvasRectSetting.maxPosition)
#RectContainer 생성
rectContainer = RectContainer(drawCanvas,canvasRectSetting,naviTileContainer)

#툴 프레임 생성
toolFrame = Frame(mainWindow,background='black')
toolFrame.pack(fill='both',side=LEFT,ipadx=400)

#제목 라벨 생성
labelText = Label(toolFrame,text="A* 알고리즘 테스트기")
labelText.pack(fill='x')

#현재 모드 라벨 생성
def ModeLabelText(stateOfInt):
    return "현재 모드 : " + EditStateText[stateOfInt]
modeLabelText = Label(toolFrame,text=ModeLabelText(9999))
modeLabelText.pack(fill='x')

#디버그 라벨 생성
clickDebugText = Label(toolFrame,text="클릭 테스트")
clickDebugText.pack(fill='x')


#캔버스 클릭 지정
def canavsClicked(event):
    temp = checkClickedPosition(Position(event.x,event.y),canvasRectSetting)
    
    clickDebugText.configure(
        text = str(event.x) + " , " + str(event.y) + " 위치 클릭 \n " 
        + str(temp.x) +" , " + str(temp.y) + "위치의 사각형 클릭" )
    if editMode.state != EditState['noneEdit']:
        rectContainer.isClicked(event,editMode.state)
def canvasMotioned(event):

    temp = checkClickedPosition(Position(event.x,event.y),canvasRectSetting)
    clickDebugText.configure(
        text = str(event.x) + " , " + str(event.y) + " 위치 클릭 \n " 
        + str(temp.x) +" , " + str(temp.y) + "위치의 사각형 위로 마우스 클릭 이동 중" )
    if editMode.state == EditState['editBrick'] or editMode.state == EditState['editDefault']:
        rectContainer.isClicked(event,editMode.state)
        


drawCanvas.bind("<Button-1>",canavsClicked)
drawCanvas.bind("<B1-Motion>",canvasMotioned)

#스타트 버튼 생성
startButton = Button(toolFrame,text="시작")
startButton.pack(fill='x')

#모드 체인지 버튼 생성
modeButton = Button(toolFrame,text="벽 편집하기")
modeButton.pack(fill='x')
def modeChange():
    if editMode.state == EditState['noneEdit']:
        editMode.state = EditState['editBrick']
        modeLabelText.configure(text = ModeLabelText(editMode.state))
        modeButton.configure(text = EditStateText[EditState['editStartPoint']])
    elif editMode.state == EditState['editBrick']:
        editMode.state = EditState['editStartPoint']
        modeLabelText.configure(text = ModeLabelText(editMode.state))
        modeButton.configure(text = EditStateText[EditState['editEndPoint']])
    elif editMode.state == EditState['editStartPoint']:
        editMode.state = EditState['editEndPoint']
        modeLabelText.configure(text = ModeLabelText(editMode.state))
        modeButton.configure(text = EditStateText[EditState['editDefault']])
    elif editMode.state == EditState['editEndPoint']:
        editMode.state = EditState['editDefault']
        modeLabelText.configure(text = ModeLabelText(editMode.state))
        modeButton.configure(text = EditStateText[EditState['noneEdit']])
    elif editMode.state == EditState['editDefault']:
        editMode.state = EditState['noneEdit']
        modeLabelText.configure(text = ModeLabelText(editMode.state))
        modeButton.configure(text = EditStateText[EditState['editBrick']])

modeButton.configure(command=modeChange)


#리셋버튼 지정
resetButton = Button(toolFrame,text = "리셋")
resetButton.pack(fill='x')
def resetButonCommand():
    rectContainer.reset()
resetButton.configure(command=resetButonCommand)

#프로그램 UI 루프 시작
mainWindow.mainloop()