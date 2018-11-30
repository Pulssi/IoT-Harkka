'''
Main module which runs the program and contains
the main loop for light toggling with speech
recognition.
'''

import RPi.GPIO as GPIO
import time
import signal
import speechToText as stt
import mqttPublish as publish

# set which pin names to use
# https://elinux.org/RPi_Low-level_peripherals
GPIO.setmode(GPIO.BCM)

# disable warnings
GPIO.setwarnings(False)

# set up pin 13 and 5 as output
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

# list of acceptable commands for toggling the light
first_light_on = ["13 1", "13 what", "13 salon", "13 Wat", "13 who won"]
second_light_on = ["5 1", "5 what", "5 salon", "5 Wat", "5 who won"]

first_light_off = ["13 4", "13 or", "13 poor"]
second_light_off = ["5 4", "5 or", "5 poor"]

# publish the initial state of the light
publish.publishMsg("light13: " + str(GPIO.input(13)))
publish.publishMsg("light5: " + str(GPIO.input(5)))

# start the mainloop
while True:
    userInput = input("Type 'y' to start or 'q' to quit\n> ")

    if (userInput == "y"):
        command = stt.speechToText()
        # for debugging purposes
        #command = input("13/5 1 or 13/5 4?")

        # determine which pin to use, 13 or 5
        if (command in first_light_on or command in first_light_off):
            pin = 13
        elif (command in second_light_on or command in second_light_off):
            pin = 5

        # determine if command is about turning light on
        if (command in first_light_on or command in second_light_on):
            if(GPIO.input(pin)):
               print("That light is already on")
            else:
                # set voltage high for the pin in use
                GPIO.output(pin, GPIO.HIGH)
                print("Light turned on!")
                publish.publishMsg("light{}: {}".format(str(pin), str(GPIO.input(pin))))

        # determine if command is about turning light off        
        elif (command in first_light_off or command in second_light_off):
            if (not GPIO.input(pin)):
               print("That light is already off")
            else:
                # set voltage low for the pin in use
                GPIO.output(pin, GPIO.LOW)
                print("Light should be now off!")
                publish.publishMsg("light{}: {}".format(str(pin), str(GPIO.input(pin))))
            
    elif (userInput == "q"):
        # reset pins
        GPIO.cleanup()
        break

print("Cleanup done, program shutting down...")
time.sleep(1)

