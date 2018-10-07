from naviContainer import *

aroundRelativePostion = 
(
    Position(-1,-1), #왼쪽위
    Position(0,-1),  #위
    Position(1,-1),  #오른쪽위
    Position(1,0),   #오른쪽
    Position(1,1),   #오른쪽아래
    Position(0,1),   #아래
    Position(-1,1),  #왼쪽아래
    Position(-1,0),  #왼쪽
)

class rectNavigationEngine:
    def __init__(self,rectContainer,naviContainer):
        self.rectContainer = rectContainer
        self.naviContainer = naviContainer
        self.openNodeList = list()
        self.closedNodeList = list()
    def getPassableList(self,x,y):
        if x < 0 or x >= self.maxX or y < 0 or y >= self.maxY:
            return None
        else:
            targetNode = self.getPosition(x,y)
            if targetNode.isPassable():
                return targetNode
            else:
                return None
    def getValidAroundPosition(self,targetNode):
        tempOpenPostionList = list()
        centerPos = PosDictToTuple(targetNode.getPosition())
        for around in aroundRelativePostion:
            tempPos = Position(around.x + centerPos.x , around.y + centerPos.y )
            if tempPos.isValid():
                tempOpenPostionList.append(tempPos)
        return tempOpenPostionList
            

    