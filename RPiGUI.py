try:
    from Tkinter import*
except ImportError:
    from tkinter import*

import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led1 = LED(23)
led2 = LED(25)
led3 = LED(20)

##GUI##
win = Tk()
win.title("LED CONTROLLER")
myFont = tkinter.font.Font(family = 'Helvetica', size = 13, weight = 'bold')

##FUNCTIONS##
def led1Toggle():
    if led1.is_lit:
        led1.off()
        
    else:
        led1.on()
        led2.off()
        led3.off()
        
def led2Toggle():
    if led2.is_lit:
        led2.off()
        
    else:
        led2.on()
        led1.off()
        led3.off()
        
def led3Toggle():
    if led3.is_lit:
        led3.off()
        
    else:
        led3.on()
        led1.off()
        led2.off()
        
def close():
    GPIO.cleanup()
    win.destroy()
    
##BUTTONS##
led1Button = Radiobutton(win, text = 'BLUE LED', value = 1, font = myFont, command = led1Toggle)
led2Button = Radiobutton(win, text = 'GREEN LED', value = 2, font = myFont, command = led2Toggle)
led3Button = Radiobutton(win, text = 'RED LED', value = 3, font = myFont, command = led3Toggle)
led1Button.grid(row = 0, column = 1)
led2Button.grid(row = 1, column = 1)
led3Button.grid(row = 2, column = 1)

exitButton = Radiobutton(win, text = 'EXIT' , value = 4, font = myFont, command = close)
exitButton.grid(row = 3, column = 1)

win.protocol("WM DELETE WINDOW", close)
win.mainloop()