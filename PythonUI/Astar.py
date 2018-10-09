from soyDebug import printDebug
from naviContainer import *
from heapq import *

aroundRelativePostion = (
    Position(0,-1),  #위
    Position(0,1),   #아래
    Position(1,0),   #오른쪽
    Position(-1,0),  #왼쪽
    Position(-1,-1), #왼쪽위
    Position(1,-1),  #오른쪽위
    Position(1,1),   #오른쪽아래
    Position(-1,1),  #왼쪽아래
)
aroundCheckPosition = (
    (),  #위
    (),   #아래
    (),   #오른쪽
    (),  #왼쪽
    (Position(0,1),Position(1,0)), #왼쪽위
    (Position(-1,0),Position(0,1)),  #오른쪽위
    (Position(-1,0),Position(0,-1)),   #오른쪽아래
    (Position(1,0),Position(0,-1))  #왼쪽아래
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
    def realStart(self):
        openList = list()
        heappush(self.naviContainer.getStartPoint())
        while END:
            targetNode = heappop(openList)
            
        #나중에 알고리즘 최적화 필요
    def getPassableNodeList(self,targetNode):
        tempOpenNodeList = list()
        #getValidAroundPosition 삽입
        tempOpenPostionList = list()
        centerPos = targetNode.getPosition()
        for around in aroundRelativePostion:
            _tempFlag = False
            tempPos = Position(around.x + centerPos.x , around.y + centerPos.y )
            tempOpenPostionList.append([tempPos,tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition)])
            printDebug('getValidAroundPosition',str(tempPos) + " / Result : " + str(tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition)))
        # tempOpenPostionList = self.getValidAroundPosition(targetNode)
        # 함수 종료
        index = 0
        for posArr in tempOpenPostionList:
            tempNode = self.naviContainer.getPosition(posArr[0])
            if posArr[1] and tempNode.isPassable():
                flag = True
                for chkPos in aroundCheckPosition[index]:
                    flag = self.naviContainer.getPosition(posArr[0] + chkPos).isPassable() and flag
                if flag:
                    tempNode.setHeuristicsValue(tempNode,self.naviContainer.getGoalPoint())
                    tempOpenNodeList.append(tempNode)
            index = index + 1
            printDebug('getPassableNodeList',str(posArr[0]) + " / Result : " + str(tempNode.isPassable()))
        return tempOpenNodeList

    # def getValidAroundPosition(self,targetNode):
    #     tempOpenPostionList = list()
    #     centerPos = targetNode.getPosition()
    #     for around in aroundRelativePostion:
    #         _tempFlag = False
    #         tempPos = Position(around.x + centerPos.x , around.y + centerPos.y )
    #         if tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition):
    #             tempOpenPostionList.append(tempPos)
    #         printDebug('getValidAroundPosition',str(tempPos) + " / Result : " + str(tempPos.isValid(self.rectContainer.canvasRectSetting.maxPosition)))
    #     return tempOpenPostionList
            

    