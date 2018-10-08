def indexToPosition(index,maxPosition):
    if index >= maxPosition.x * maxPosition.y:
        raise Exception('indexOverFlow!! / index is over to max-index:(maxX*maxY)') 
    return Position(index % maxPosition.x,index // maxPosition.y)

class Position:
    def __init__(self,x = -1,y = -1):
        self.x = x
        self.y = y
    def isValid(self,maxPosition):
        return not (self.x < 0 or self.x >= maxPosition.x or self.y < 0 or self.y >= maxPosition.y)
    def toIndex(self,maxPosition):
        return self.y * maxPosition.y + self.x
    def __str__(self):
        return "x : {} , y : {}".format(self.x,self.y)