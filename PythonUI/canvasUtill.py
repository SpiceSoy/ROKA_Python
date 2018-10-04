from positionUtill import InversionPosition

class CanvasRectSetting:
    def __init__(self,marginX,marginY,rectSize,rectMax):
            self.marginX = marginX
            self.marginY = marginY
            self.rectSize = rectSize
            self.rectMax = rectMax 

def calcIndex(x,y,canvasRectSetting):
    # canvasRectSetting = CanvasRectSetting(canvasRectSetting)
    x = x - canvasRectSetting.marginX 
    y = y - canvasRectSetting.marginY
    xIndex = x // canvasRectSetting.rectSize
    yIndex = y // canvasRectSetting.rectSize
    if canvasRectSetting.rectMax <= xIndex or xIndex < 0 :
        xIndex = -1
        yIndex = -1
    if canvasRectSetting.rectMax <= yIndex or yIndex < 0 :
        xIndex = -1
        yIndex = -1
    return (xIndex,yIndex)
def checkIndex(checkList):
    return (checkList[1] != -1 or checkList[0] != -1)