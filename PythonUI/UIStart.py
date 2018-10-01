from tkinter import *
from RectClass import *


mainWindow = Tk()

mainWindow.title("알고리즘 공부합시다!")
mainWindow.geometry("1100x783+50+15")
mainWindow.resizable(False,False)


drawCanvas = Canvas(mainWindow,width=780,height=780)
drawCanvas.pack(side=LEFT)
drawCanvas.configure(background='black')

rectMax = 25
rectSize = 30

# for xCount in range(rectMax): 
#     for yCount in range(rectMax):
#         drawCanvas.create_rectangle(
#             xCount*rectSize + rectSize/2,
#             yCount*rectSize + rectSize/2,
#             (xCount+1)*rectSize + rectSize/2,
#             (yCount+1)*rectSize + rectSize/2,
#             fill='gray')

rectList = list()
for yCount in range(rectMax):
    tempYlist = list()
    for xCount in range(rectMax): 
        tempYlist.append(Rect(drawCanvas,xCount,yCount,rectSize,15,15,'white'))
    rectList.append(tempYlist)

        



toolFrame = Frame(mainWindow,background='black')
toolFrame.pack(fill='both',side=LEFT,ipadx=400)

labelText = Label(toolFrame,text="A* 알고리즘 테스트기")
labelText.pack(fill='x')
startButton = Button(toolFrame,text="시작")
startButton.pack(fill='x')

mainWindow.mainloop()