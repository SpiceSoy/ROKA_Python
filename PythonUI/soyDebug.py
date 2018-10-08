
#플래그 값 들

flag = {
    'default' : True,
    'getPassableNodeList' : True,
    'getValidAroundPosition' : True,
    'passableResult' : True
}

def printDebug(flagStr,_str):
    if flag[flagStr]:
        if(flagStr != ''):
            _str = flagStr + " : " + _str
        print(_str)
