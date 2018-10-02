from tkinter import *

class Rect:
    def __init__(self,canvas,containList,xIndex,yIndex,canvasRectSetting,color='green'):
        self.parentCanvas = canvas
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.color = color
        self.canvasRectSetting = canvasRectSetting
        self.containList = containList
        self.__drawInCanvas()

    def __drawInCanvas(self):
            self.parentCanvas.create_rectangle(
            self.canvasRectSetting.marginX + self.xIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + self.yIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginX + (self.xIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + (self.yIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            fill=self.color
            )
    def __getCenterPointX(self):
            return self.marginX + (self.xIndex * self.rectSize) + (self.rectSize/2)
    def __getCenterPointY(self):
            return self.marginY + (self.yIndex * self.rectSize) + (self.rectSize/2)
    def Refresh(self):
        self.__drawInCanvas()
    def isClicked(self,event,state = 'edit'):
        #Edit 모드일때는 클릭시 붉은색으로 변화합니다.
        if state == 'edit':
            self.color = 'gray'
            self.Refresh()
        