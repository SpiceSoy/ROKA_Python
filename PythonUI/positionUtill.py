def indexToPosition(index,maxX,maxY):
    if index >= maxX*maxY:
        raise Exception('indexOverFlow!! / index is over to max-index:(maxX*maxY)') 
    x = index % maxY
    y = index // maxY
    return {'x': x, 'y' : y}
def positionToIndex(x,y,maxX,maxY):
    return y*maxY + x