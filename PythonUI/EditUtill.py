EditState = {
    'editDefault':0,
    'editBrick':1,
    'editStartPoint':2,
    'editEndPoint':3,
    'noneEdit':9999
    }

EditStateText = {
    0:"길 편집 모드",
    1:"벽 편집 모드",
    2:"시작지점 편집 모드",
    3:"종료지점 편집 모드",
    9999:"대기 모드",
}

class EditMode:
    def __init__(self,state):
        self.state = state