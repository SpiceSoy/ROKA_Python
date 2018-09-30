from tkinter import *

mainWindow = Tk()

mainWindow.title("알고리즘 공부합시다!")
mainWindow.geometry("1100x783+50+15")
mainWindow.resizable(False,False)

drawCanvas = Canvas(mainWindow,width=780,height=780)
drawCanvas.place(x=0,y=0)
drawCanvas.configure(background='black')

rectMax = 25
rectSize = 30

for xCount in range(rectMax): 
    for yCount in range(rectMax):
        drawCanvas.create_rectangle(
            xCount*rectSize + rectSize/2,
            yCount*rectSize + rectSize/2,
            (xCount+1)*rectSize + rectSize/2,
            (yCount+1)*rectSize + rectSize/2,
            fill='gray')

startButton = Button(mainWindow,text="시작",width=40)
startButton.place(x=790,y=15)

mainWindow.mainloop()