import time
from tkinter import *
from plyer import notification

def eyeRest():
        while True:
                notification.notify(
                app_icon ="C:/Users/santo/Desktop/Python A/Ass 4/eye.ico",
                title = "Please rest your eyes",
                message = "20 min reminder to look at something 20 meters away for 20 seconds",
                timeout=10
                )
                time.sleep(15)

def pomodoro():
        while True:
                notification.notify(
                        app_icon ="C:/Users/santo/Desktop/Python A/Ass 4/pomodoro.ico",
                        title = "Study Timer Activated",
                        message = "25 min study time and 5 min break time",
                        timeout=10
                        )
                time.sleep(15)
                notification.notify(
                        app_icon ="C:/Users/santo/Desktop/Python A/Ass 4/pomodoro.ico",
                        title = "BREAK TIME",
                        message = "5 min break time starts now!",
                        timeout=10
                        )
                time.sleep(20)
        

menuGUI = Tk()

menuOptions = Menu(menuGUI)
menuGUI.config(menu=menuOptions)

options = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="Button 1",menu=options)
options.add_command(label="Eye rest",command=eyeRest)

options = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="Button 2",menu=options)
options.add_command(label="Pomodoro",command=pomodoro)

menuGUI.mainloop()

