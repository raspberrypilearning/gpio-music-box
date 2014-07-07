#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import pygame.mixer

#For Arduino LEDS
import smbus
import time
bus = smbus.SMBus(1)
# I2c Address:
address = 0x04


pygame.mixer.init(44000, -16, 2, 500)

GPIO.setmode(GPIO.BCM)

# 25 to stop the script
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Point at sound files
soundA = pygame.mixer.Sound("note_a.wav")
soundB = pygame.mixer.Sound("note_b.wav")
soundC = pygame.mixer.Sound("note_c.wav")
soundD = pygame.mixer.Sound("note_d.wav")
soundE = pygame.mixer.Sound("note_e.wav")
soundF = pygame.mixer.Sound("note_f.wav")

SOUND_PINS = {
    17: soundA,
    18: soundB,
    27: soundC,
    22: soundD,
    23: soundE,
    24: soundF
}

# Define the setup function: activate pin, loop sound indefinitely, mute, GPIO event detection
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
    sound = SOUND_PINS[pin]
    sound.play(loops=-1)
    sound.set_volume(0)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=pin_change, bouncetime=0)

# Define the callback function: Set volume according to GPIO pin status
def pin_change(pin):
    sound = SOUND_PINS[pin]
    volume = GPIO.input(pin)
    sound.set_volume(volume)
    writeNumber(pin)
    state = "high" if volume else "low"
    print "Pin %s is %s" % (pin, state)
    time.sleep(1)
    number = readNumber()
    print "Arduino: Hey RPI, I received a digit ", number

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def main():
    map(pin_change, SOUND_PINS)

    print "Waiting for Pin 25 to end script."
    GPIO.wait_for_edge(25, GPIO.RISING)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
