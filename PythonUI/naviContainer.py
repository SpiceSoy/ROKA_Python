from positionUtill import *

NodeState = {'default':0,'brick':1,'startPoint':2,'goalPoint':3}
StatePassable = {0:True,1:False,2:True,3:True}
StateColor = {0:'white',1:'gray',2:'lightgreen',3:'gold'}

def defaultRefreshFunc():
    return None
#네비게이션 최소단위 노드입니다. RectClass와 분리합니다.
class naviNode:
    def __init__(self,state = NodeState['default'],refreshFunc = defaultRefreshFunc):
        self.state = state
        self.refreshFunc = refreshFunc
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
    def __init__(self,index,maxX,maxY,state = NodeState['default']):
        super().__init__(state)
        self.x = indexToPosition(index,maxX,maxY)['x']
        self.y = indexToPosition(index,maxX,maxY)['y']
        self.index = index
    def getPosition(self):
        return {'x':self.x,'y':self.y}

#StartPoint 와 GoalPoint 갯수를 한정하기 위한 플래그입니다.
class NowPoint:
    def __init__(self):
        self.nowStartPoint = naviNode(NodeState['startPoint'])  
        self.nowGoalPoint = naviNode(NodeState['goalPoint'])
nowPoint = NowPoint()

def isChangeState(state,node):
    if state == NodeState['startPoint']:
        nowPoint.nowStartPoint.reset()
        nowPoint.nowStartPoint = node
    elif  state == NodeState['goalPoint']:
        nowPoint.nowGoalPoint.reset()
        nowPoint.nowGoalPoint = node


class NaviTileContainer:
    def __init__(self,maxX,maxY):
        self.maxX = maxX
        self.maxY = maxY
        self.__containerInitialize(maxX,maxY)
    def __containerInitialize(self,maxX,maxY):
        self.nodeContainer = list()
        for i in range(0,maxX*maxY):
            self.nodeContainer.append( naviTile(i,maxX,maxY))
    def getPosition(self,x,y):
        return self.nodeContainer[y*maxY + x]
    def getIndex(self,index):
        return self.nodeContainer[index]
    
    