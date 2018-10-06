from tkinter import *
import ctypes
user = ctypes.windll.user32

HEX = 0xAD #가상키 코드
def mute(event):
    user.keybd_event(HEX,0,1,0) #키 내리기
    user.keybd_event(HEX,0,2,0) #키 올리기

#메인 윈도우 생성
mainWindow = Tk()
mainWindow.title("사지방 음소거")
mainWindow.geometry("100x100+1300+700")
mainWindow.resizable(False,False)


startButton = Button(mainWindow,text="Mute!!")
startButton.pack(fill='both',expand=True)

startButton.bind("<Button-1>",mute)


Toplevel.transient(mainWindow)

mainWindow.wm_attributes("-topmost", 1)

mainWindow.mainloop()