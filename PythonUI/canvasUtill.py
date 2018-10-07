from positionUtill import *

class CanvasRectSetting:
    def __init__(self,marginX,marginY,rectSize,maxX,maxY):
            self.margin = Position(marginX,marginY)
            self.rectSize = rectSize
            self.maxPosition = Position(maxX,maxY)

def checkClickedPosition(position,canvasRectSetting):
    # canvasRectSetting = CanvasRectSetting(canvasRectSetting)
    position.x = position.x - canvasRectSetting.margin.x
    position.y = position.y - canvasRectSetting.margin.y
    index = Position(position.x // canvasRectSetting.rectSize , position.y // canvasRectSetting.rectSize)
    if canvasRectSetting.maxPosition.x <= index.x or index.x < 0 or canvasRectSetting.maxPosition.y <= index.y or index.y < 0 :
        index.x = -1
        index.y = -1
    return index
def checkClickedIndex(position,canvasRectSetting):
    position = checkClickedPosition(position,canvasRectSetting)
    return position.toIndex(canvasRectSetting.maxPosition)
