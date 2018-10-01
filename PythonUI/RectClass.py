from tkinter import *

class Rect:
    def __init__(self,canvas,xIndex,yIndex,rectSize,marginX = 0 ,marginY = 0,color='green'):
        self.parentCanvas = canvas
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.rectSize = rectSize
        self.color = color
        self.marginX = marginX
        self.marginY = marginY
        self.__drawInCanvas()

    def __drawInCanvas(self):
            self.parentCanvas.create_rectangle(
            self.marginX + self.xIndex * self.rectSize,
            self.marginY + self.yIndex * self.rectSize,
            self.marginX + (self.xIndex * self.rectSize) + self.rectSize,
            self.marginY + (self.yIndex * self.rectSize) + self.rectSize,
            fill=self.color
            )