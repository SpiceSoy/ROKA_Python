def InversionPosition(index,maxX,maxY):
    if index >= maxX*maxY:
        raise Exception('indexOverFlow!! / index is over to max-index:(maxX*maxY)') 
    x = index % maxY
    y = index // maxY
    return {'x': x, 'y' : y}

index = int(input('index : '))
maxX = int(input('Max X : '))
maxY = int(input('Max y : '))

result = InversionPosition(index,maxX,maxY)
print("x : " + str(result['x']) + ", y : " + str(result['y']) + " / end")
