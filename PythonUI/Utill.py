from enum import *

EditState = {'default':1,'editBlock':2,'editStartPoint':3,'editEndPoint':4}
RectState = {'default':1,'block':2,'startPoint':3,'endPoint':4}
class EditMode:
    def __init__(self,state):
        self.state = state


StartPoint = [-1,-1]
EndPoint = [-1,-1]