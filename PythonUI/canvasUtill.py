from positionUtill import *

class CanvasRectSetting:
    def __init__(self,marginX,marginY,rectSize,maxX,maxY):
            self.marginX = marginX
            self.marginY = marginY
            self.rectSize = rectSize
            self.maxX = maxX
            self.maxY = maxY

def checkClickedPosition(x,y,canvasRectSetting):
    # canvasRectSetting = CanvasRectSetting(canvasRectSetting)
    x = x - canvasRectSetting.marginX 
    y = y - canvasRectSetting.marginY
    xIndex = x // canvasRectSetting.rectSize
    yIndex = y // canvasRectSetting.rectSize
    if canvasRectSetting.maxX <= xIndex or xIndex < 0 :
        xIndex = -1
        yIndex = -1
    if canvasRectSetting.maxY <= yIndex or yIndex < 0 :
        xIndex = -1
        yIndex = -1
    return {'x':xIndex,'y':yIndex}
def isPositionValid(checkList):
    return (checkList['x'] != -1 or checkList['y'] != -1)
def checkClickedIndex(x,y,canvasRectSetting):
    position = checkClickedPosition(x,y,canvasRectSetting)
    return positionToIndex(position['x'],position['y'],canvasRectSetting.maxX,canvasRectSetting.maxY)
