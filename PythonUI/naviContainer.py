from positionUtill import InversionPosition

NodeState = {'default':0,'brick':1,'startPoint':2,'goalPoint':3}
StatePassable = {0:True,1:False,2:True,3:True}
StateColor = {0:'white',1:'gray',2:'lightgreen',3:'gold'}

#네비게이션 최소단위 노드입니다. RectClass와 분리합니다.
class naviNode:
    def __init__(self,state = NodeState['default']):
        self.state = NodeState
    def isPassable(self):
        return StatePassable[self.state]
    def isGoalPoint(self):
        return state == NodeState['goalPoint']
    def getColor(self):
        return StateColor[self.state]
    def changeState(self,stateOfint):
        self.state = stateOfint

class naviTile(naviNode):
    def __init__(self,index,maxX,maxY,state = NodeState['default']):
        super(naviNode).__init__(state)
        self.x = InversionPosition(index,maxX,maxY)['x']
        self.y = InversionPosition(index,maxX,maxY)['y']
        self.index = index
    def getPosition(self):
        return {'x':self.x,'y':self.y}
    

class NaviTileContainer:
    def __init__(self,maxX,maxY):
        self.maxX = maxX
        self.maxY = maxY
    def __containerInitialize(self,maxX,maxY):
        self.nodeContainer = list()
        for i in range(0,maxX*maxY):
            self.nodeContainer.append( naviTile() )
    def getPosition(self,x,y):
        return self.nodeContainer[y*maxY + x]
    
    