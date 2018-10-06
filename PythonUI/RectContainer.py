from tkinter import *
from EditUtill import *
from canvasUtill import *
from naviContainer import *




class Rect:
    def __init__(self,index,canvas,canvasRectSetting,tileNode):
        self.tileNode = tileNode
        self.targetCanvas = canvas
        self.canvasRectSetting = canvasRectSetting
        self.index = index
        tempPosition = indexToPosition(index,canvasRectSetting.maxX,canvasRectSetting.maxY)
        self.xIndex = tempPosition['x']
        self.yIndex = tempPosition['y']
        self.__drawInCanvas()

    def __drawInCanvas(self):
            self.targetCanvas.create_rectangle(
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
        # self.Refresh()
    def reset(self):
        self.tileNode.reset()
        # self.Refresh()
    def getRefresher(self):
        return self.Refresh

class RectContainer:
    def __init__(self,canvas,canvasRectSetting,naviTileContainer):
        self.targetCanvas = canvas
        self.canvasRectSetting = canvasRectSetting
        self.naviTileContainer = naviTileContainer
        self.__containerInitialize(canvasRectSetting.maxX,canvasRectSetting.maxY)
    def __containerInitialize(self,maxX,maxY):
        self.rectContainer = list()
        for i in range(self.canvasRectSetting.maxX * self.canvasRectSetting.maxY):
            self.rectContainer.append( Rect(i,self.targetCanvas,self.canvasRectSetting,self.naviTileContainer.getIndex(i)) )
            self.naviTileContainer.getIndex(i).SetRefresher(self.getIndex(i).getRefresher())
    def getPosition(self,x,y):
        return self.rectContainer[y*canvasRectSetting.maxY + x]
    def getIndex(self,index):
        return self.rectContainer[index]
    def GetClickedObject(self,x,y):
            return self.getIndex(checkClickedIndex(x,y,self.canvasRectSetting))
    def isClicked(self,event,state):
            self.GetClickedObject(event.x,event.y).isClicked(event,state)
    def reset(self):
        for rect in self.rectContainer:
            rect.reset()
