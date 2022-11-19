#import time
from tkinter import *
#from plyer import notification

menuGUI = Tk()

menuOptions = Menu(menuGUI)
menuGUI.config(menu=menuOptions)

option1 = Menu(menuOptions)
menuOptions.add_cascade(label="Button 1",menu=option1)

menuGUI.mainloop()

#while True:
        #notification.notify(
                #app_icon ="C:/Users/santo/Desktop/Python A/Ass 4/icon.ico",
                #title = "Please rest your eyes",
               # message = "20 min reminder to look at something 20 meters away for 20 seconds",
                #timeout=10
                #)
        #time.sleep(30)

