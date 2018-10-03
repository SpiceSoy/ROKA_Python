from tkinter import *
from Utill import *


def swtichColor(state):
    if state == RectState['block']:
        print("Draw gray")
        return 'gray'
    elif state == RectState['startPoint']:
        print("Draw lightgreen")
        return 'lightgreen'
    elif state == RectState['endPoint']:
        print("Draw gold")
        return 'gold'
    else:
        return 'white'

class Rect:
    def __init__(self,canvas,containList,xIndex,yIndex,canvasRectSetting,state=RectState['default']):
        self.parentCanvas = canvas
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.state = state
        self.canvasRectSetting = canvasRectSetting
        self.containList = containList
        self.__drawInCanvas()

    def __drawInCanvas(self):
            self.parentCanvas.create_rectangle(
            self.canvasRectSetting.marginX + self.xIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + self.yIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginX + (self.xIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + (self.yIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            fill = swtichColor(self.state)
            )
    def __getCenterPointX(self):
            return self.marginX + (self.xIndex * self.rectSize) + (self.rectSize/2)
    def __getCenterPointY(self):
            return self.marginY + (self.yIndex * self.rectSize) + (self.rectSize/2)
    def Refresh(self):
        self.__drawInCanvas()
    def isClicked(self,event,state):
        self.state = state
        self.Refresh()
        