# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

phase = 11
enable = 12
direction = 13

GPIO.setup(phase,GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(direction,GPIO.IN, pull_up_down=GPIO.PUD_UP)

enable_motor = GPIO.PWM(enable, 50)

def drive_motor():
        enable_motor.start(100)

def set_direction():
        if GPIO.input(direction) == True:
                GPIO.output(phase,True)
                print "eteen"
        elif GPIO.input(direction) == False:
                GPIO.output(phase,False)
                print "taakse"
        else: print "Error"

def start():
        while True:
                set_direction()
                time.sleep(1)
                drive_motor()

def stop():
        enable_motor.start(0)
        enable_motor.stop()
'''
start()
'''
stop()

