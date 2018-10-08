from soyDebug import printDebug
from naviContainer import *

aroundRelativePostion = (
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
    def start(self):
        temp = self.getPassableNodeList(self.naviContainer.getStartPoint())
        printDebug('passableResult',str(len(temp)))
    def getPassableNodeList(self,targetNode):
        tempOpenNodeList = list()
        tempOpenPostionList = self.getValidAroundPosition(targetNode)
        for pos in tempOpenPostionList:
            tempNode = self.naviContainer.getPosition(pos)
            if tempNode.isPassable():
                tempOpenNodeList.append(tempNode)
            printDebug('getPassableNodeList',str(pos) + " / Result : " + str(tempNode.isPassable()))
        return tempOpenNodeList
    
    # 이게문제
    def getValidAroundPosition(self,targetNode):
        tempOpenPostionList = list()
        centerPos = targetNode.getPosition()
        for around in aroundRelativePostion:
            _tempFlag = False
            tempPos = Position(around.x + centerPos.x , around.y + centerPos.y )
            if tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition):
                tempOpenPostionList.append(tempPos)
            printDebug('getValidAroundPosition',str(tempPos) + " / Result : " + str(tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition)))
        return tempOpenPostionList
            

    