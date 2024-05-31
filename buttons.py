import RPi.GPIO as GPIO
import time
import os
from subprocess import Popen, PIPE, STDOUT

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)

def turnOnScreen():
    os.system('raspi-gpio set 19 op a5')
    GPIO.output(18, GPIO.HIGH)
    stop_and_change_video()


def turnOffScreen():
    os.system('raspi-gpio set 19 ip')
    GPIO.output(18, GPIO.LOW)


def stop_and_change_video():
    # Comunicar con player.py para detener el video actual
    os.system('pkill -f mplayer')    


turnOffScreen()
screen_on = False

while (True):
    # If you are having and issue with the button doing the opposite of what you want
    # IE Turns on when it should be off, change this line to:
    # input = not GPIO.input(26)
    input = GPIO.input(26)
    if input != screen_on:
        screen_on = input
        if screen_on:
            turnOnScreen()
        else:
            turnOffScreen()
    time.sleep(0.3)
