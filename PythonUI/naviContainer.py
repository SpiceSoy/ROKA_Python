from positionUtill import *

NodeState = {'default':0,'brick':1,'startPoint':2,'goalPoint':3 , 'passedPoint':4,'None' : 999}
StatePassable = {0:True,1:False,2:True,3:True,4:False,999:False}
StateColor = {0:'white',1:'gray',2:'lightgreen',3:'gold',4:'aqua',999:'pink'}

def defaultRefreshFunc():
    return None
#네비게이션 최소단위 노드입니다. RectClass와 분리합니다.
class naviNode:
    def __init__(self,state = NodeState['default'],refreshFunc = defaultRefreshFunc):
        self.state = state
        self.refreshFunc = refreshFunc
        #AstarEngine 이후 추가된 것
        self.previousPassNode = naviNode(NodeState['None'])
    def isPassable(self):
        return StatePassable[self.state]
    def isGoalPoint(self):
        return state == NodeState['goalPoint']
    def getColor(self):
        return StateColor[self.state]
    def changeState(self,stateOfint):
        self.state = stateOfint
        isChangeState(self.state,self)
        self.refreshFunc()
    def reset(self):
        self.state = NodeState['default']
        self.refreshFunc()
    def SetRefresher(self,refreshFunc):
        self.refreshFunc = refreshFunc

class naviTile(naviNode):
    def __init__(self,index,maxPosition,state = NodeState['default']):
        super().__init__(state)
        self.position = indexToPosition(index,maxPosition)
        self.index = index
    def getPosition(self):
        return self.position

#StartPoint 와 GoalPoint 갯수를 한정하기 위한 플래그입니다.
class NowPoint:
    def __init__(self):
        self.nowStartPoint = naviNode(NodeState['None'])  
        self.nowGoalPoint = naviNode(NodeState['None'])
nowPoint = NowPoint()

def isChangeState(state,node):
    if state == NodeState['startPoint']:
        nowPoint.nowStartPoint.reset()
        nowPoint.nowStartPoint = node
    elif  state == NodeState['goalPoint']:
        nowPoint.nowGoalPoint.reset()
        nowPoint.nowGoalPoint = node


class NaviTileContainer:
    def __init__(self,maxPosition):
        self.maxPosition = maxPosition
        self.__containerInitialize()
    def __containerInitialize(self):
        self.nodeContainer = list()
        for i in range(0,self.maxPosition.x*self.maxPosition.y):
            self.nodeContainer.append( naviTile(i,self.maxPosition))
    def getIndex(self,index):
        return self.nodeContainer[index]
    def getPosition(self,position):
        return self.getIndex(position.toIndex(self.maxPosition))
    def getStartPoint(self):
        return nowPoint.nowStartPoint
    def getGoalPoint(self):
        return nowPoint.nowGoalPoint

    