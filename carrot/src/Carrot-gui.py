from tkinter import *
import threading
from time import sleep

class Window:
    def __init__(self):
        self.flg = False
        self.root = Tk()
        self.LiPo = DoubleVar()
        self.motor_x = DoubleVar()
        self.motor_y = DoubleVar()
        self.EMERGENCY = BooleanVar()
        self.LiPo.set(25)
        self.motor_x.set(0.0)
        self.motor_y.set(0.0)
        self.EMERGENCY.set(False)
        Voltage=Label(self.root, textvariable=self.LiPo)
        Voltage.place(x=100,y=10)
        Volt=Label(self.root, text="V",font=(20))
        Volt.place(x=120,y=10)
        X_dic=Label(self.root, textvariable=self.motor_x)
        X_dic.place(x=100,y=40)
        Y_dic=Label(self.root, textvariable=self.motor_y)
        Y_dic.place(x=100,y=60)
        EME=Label(self.root, textvariable=self.EMERGENCY)
        EME.place(x=100,y=80)

        label=[Voltage,X_dic,Y_dic,EME]

        self.root.title(u"Carrot Debug Terminal v0.1")
        self.root.geometry("400x300")

        self.loop()

    def loop(self):
        t = threading.Thread(target=FunctionThatTakeALotOfTime, args=(self,))
        t.start()

def FunctionThatTakeALotOfTime(w):
    i=0
    while True:
        i+=1
        w.txt.set(str(i))
        sleep(0.5)

if __name__ == '__main__':
    w = Window()
    w.root.mainloop()