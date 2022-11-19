import time
from tkinter import *
from plyer import notification

#Functions for specific timers. This is a looping timer which notifies you about when to take a break depending on what program selected
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

#About info on why this program is created and its contents
def about():
    print("\n\nThis Program is designed to help students/people who work on computers by preventing them from eyestrains and/or mind blanks and fatigue. Inside the GUI")
    print("you can see that there are 2 options one for 'Eye strain' and one 'Pomodoro'. Now what do these mean? Essentially, Eye strain implements the 20-20-20 rule which is")
    print("to rest your eyes every 20 mins and look at something 20 meters away for 20 seconds. By doing this you will prevent eye strain and can efficiently study/work on the computer")
    print("without getting tired. Pomodoro is a study timer which implements the Pomodomo rule which are 25 min study time and then take 5 min breaks in between them.")
    print("Essentially with this, you wouldn't go into over-studying to the point of being tired or not being able to understand anything at all because of long periods of studying.")  
    print("\n ** Note that this code doesn't implement real time timers. This is because for easy debugging and testing to see the results more sooner than having to wait the real required minutes. **") 

#Simple gui creation using Tkinter
menuGUI = Tk()

menuOptions = Menu(menuGUI)
menuGUI.config(menu=menuOptions)

#cascade option for eye rest program
options = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="Eye Rest",menu=options)
options.add_command(label="Start",command=eyeRest)

#cascade option for pomodoro program
options = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="Pomodoro",menu=options)
options.add_command(label="Start",command=pomodoro)

#cascade option for bringing up about text
options = Menu(menuOptions,tearoff=0)
menuOptions.add_cascade(label="About",menu=options)
options.add_command(label="Show Text",command=about)

menuGUI.mainloop()
