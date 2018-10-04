from tkinter import *
from EditUtill import *
from naviContainer import naviNode




class Rect:
    def __init__(self,canvas,canvasRectSetting,tileNode):
        self.tileNode = tileNode
        self.canvas = canvas
        self.canvasRectSetting = canvasRectSetting

    def __drawInCanvas(self):
            self.parentCanvas.create_rectangle(
            self.canvasRectSetting.marginX + self.xIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + self.yIndex * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginX + (self.xIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            self.canvasRectSetting.marginY + (self.yIndex * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            fill = self.tileNode.getColor()
            )
    def __getCenterPointX(self):
            return self.marginX + (self.tileNode.getPosition()['x'] * self.canvasRectSetting.rectSize) + (self.canvasRectSetting.rectSize/2)
    def __getCenterPointY(self):
            return self.marginY + (self.tileNode.getPosition()['y'] * self.canvasRectSetting.rectSize) + (self.canvasRectSetting.rectSize/2)
    def Refresh(self):
        self.__drawInCanvas()
    def isClicked(self,event,state):
        self.tileNode.changeState(state)
        self.Refresh()
        