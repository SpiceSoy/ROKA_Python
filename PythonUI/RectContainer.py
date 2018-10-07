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
        self.position = indexToPosition(index,canvasRectSetting.maxPosition)
        self.__drawInCanvas()

    def __drawInCanvas(self):
            self.targetCanvas.create_rectangle(
            self.canvasRectSetting.margin.x + self.position.x * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.margin.y + self.position.y * self.canvasRectSetting.rectSize,
            self.canvasRectSetting.margin.x + (self.position.x * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            self.canvasRectSetting.margin.y + (self.position.y * self.canvasRectSetting.rectSize) + self.canvasRectSetting.rectSize,
            fill = self.tileNode.getColor()
            )
    def __getCenterPointX(self):
            return self.marginX + (self.tileNode.getPosition().x * self.canvasRectSetting.rectSize) + (self.canvasRectSetting.rectSize/2)
    def __getCenterPointY(self):
            return self.marginY + (self.tileNode.getPosition().y * self.canvasRectSetting.rectSize) + (self.canvasRectSetting.rectSize/2)
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
        self.__containerInitialize()
    def __containerInitialize(self):
        self.rectContainer = list()
        for i in range(self.canvasRectSetting.maxPosition.x * self.canvasRectSetting.maxPosition.y):
            self.rectContainer.append( Rect(i,self.targetCanvas,self.canvasRectSetting,self.naviTileContainer.getIndex(i)) )
            self.naviTileContainer.getIndex(i).SetRefresher(self.getIndex(i).getRefresher())
    def getPosition(self,position):
        return self.rectContainer[position.y*canvasRectSetting.maxPosition.y + position.x]
    def getIndex(self,index):
        return self.rectContainer[index]
    def GetClickedObject(self,position):
            return self.getIndex(checkClickedIndex(position,self.canvasRectSetting))
    def isClicked(self,event,state):
            self.GetClickedObject(Position(event.x,event.y)).isClicked(event,state)
    def reset(self):
        for rect in self.rectContainer:
            rect.reset()
