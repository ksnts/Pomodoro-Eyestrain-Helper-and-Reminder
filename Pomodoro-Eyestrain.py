import time
from tkinter import *
from plyer import notification

def eyeRest():
        while True:
                notification.notify(
                app_icon ="C:/Users/santo/Desktop/Python A/Ass 4/icon.ico",
                title = "Please rest your eyes",
                message = "20 min reminder to look at something 20 meters away for 20 seconds",
                timeout=10
                )
                time.sleep(30)

menuGUI = Tk()

menuOptions = Menu(menuGUI)
menuGUI.config(menu=menuOptions)

option1 = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="Button 1",menu=option1)
option1.add_command(label="Eye rest",command=eyeRest)

menuGUI.mainloop()



