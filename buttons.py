import RPi.GPIO as GPIO
import time
import os

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)


def turnOnScreen():
    GPIO.output(18, GPIO.HIGH)
    os.system('pkill -f mplayer')


def turnOffScreen():
    GPIO.output(18, GPIO.LOW)


turnOffScreen()
screen_on = False

while (True):
    input = GPIO.input(25)
    if input != screen_on:
        screen_on = input
        if screen_on:
            turnOnScreen()
        else:
            turnOffScreen()
    time.sleep(0.3)