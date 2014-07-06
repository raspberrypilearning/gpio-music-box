#!/usr/bin/env python2.7  
  
import RPi.GPIO as GPIO 
import time
import pygame.mixer

pygame.mixer.init(44000, -16, 2, 500) 

GPIO.setmode(GPIO.BCM)  
  
# 25 to stop the script  
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# 3V3 (3.3V) to 17, 18, 27, 22, 23, 24 
# to play notes  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time_stamp = time.time()  

# Point at sound files
soundA = pygame.mixer.Sound("note_a.wav") 
soundB = pygame.mixer.Sound("note_b.wav")
soundC = pygame.mixer.Sound("note_c.wav")
soundD = pygame.mixer.Sound("note_d.wav") 
soundE = pygame.mixer.Sound("note_e.wav")
soundF = pygame.mixer.Sound("note_f.wav")

# Loop all sounds
soundA.play(loops=-1)
soundB.play(loops=-1)
soundC.play(loops=-1)
soundD.play(loops=-1)
soundE.play(loops=-1)
soundF.play(loops=-1)

SOUND_PINS = {
	17: soundA,
	18: soundB,
	27: soundC,
	22: soundD,
	23: soundE,
	24: soundF
}

# Mute all Sounds
soundA.set_volume(0.0)
soundB.set_volume(0.0)
soundC.set_volume(0.0)
soundD.set_volume(0.0)
soundE.set_volume(0.0)
soundF.set_volume(0.0)

# Define the callback functions: Turn Volume up to 100% 


def note_on(pin):
	sound = SOUND_PINS[pin]
	sound.set_volume(1.0)
	print "Note %s playing" % pin
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected, regardless of whatever   
# else is happening in the program, the notes will be run  
# It will happen even while the program is waiting for  
# a raising edge on Pin 25.  

GPIO.add_event_detect(17, GPIO.RISING, callback=note_on, bouncetime=200)  
GPIO.add_event_detect(18, GPIO.RISING, callback=note_on, bouncetime=200)
GPIO.add_event_detect(27, GPIO.RISING, callback=note_on, bouncetime=200)  
GPIO.add_event_detect(22, GPIO.RISING, callback=note_on, bouncetime=200)  
GPIO.add_event_detect(23, GPIO.RISING, callback=note_on, bouncetime=200)  
GPIO.add_event_detect(24, GPIO.RISING, callback=note_on, bouncetime=200)   
 
print "Pin 25 pressed - script end."
GPIO.wait_for_edge(25, GPIO.RISING)

GPIO.cleanup()