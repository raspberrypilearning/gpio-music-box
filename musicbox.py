#!/usr/bin/env python2.7  
  
import RPi.GPIO as GPIO 
import time 
import os
import pygame.mixer

pygame.mixer.init(44000, -16, 1, 1024) 

GPIO.setmode(GPIO.BCM)  
  
# 25 to stop the script  
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# 3V3 (3.3V)  to 17, 18, 27, 22, 23, 24 
# to play notes  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time_stamp = time.time()  


soundA = pygame.mixer.Sound("note_a.wav") 
soundB = pygame.mixer.Sound("note_b.wav")
soundC = pygame.mixer.Sound("note_c.wav")
soundD = pygame.mixer.Sound("note_d.wav") 
soundE = pygame.mixer.Sound("note_e.wav")
soundF = pygame.mixer.Sound("note_f.wav")

soundChannelA = pygame.mixer.Channel(1) 
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
soundChannelD = pygame.mixer.Channel(4) 
soundChannelE = pygame.mixer.Channel(5)
soundChannelF = pygame.mixer.Channel(6)



# Define the callback functions (notes)    
def note_a(channel): 
	soundChannelA.play(soundA)
	print "Note A playing"
def note_b(channel):
	soundChannelB.play(soundB)  
	print "Note B playing"
def note_c(channel):  
	soundChannelC.play(soundC)
	print "Note C playing"
def note_d(channel):  
	soundChannelD.play(soundD) 
	print "Note D playing"
def note_e(channel):  
	soundChannelE.play(soundE) 
	print "Note E playing"
def note_f(channel):  
	soundChannelF.play(soundF) 
	print "Note F playing"

raw_input("Press Enter to start\n>")  
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected, regardless of whatever   
# else is happening in the program, the notes will be run  
# It will happen even while the program is waiting for  
# a raising edge on Pin 25.  

GPIO.add_event_detect(17, GPIO.RISING, callback=note_a, bouncetime=200)  
GPIO.add_event_detect(18, GPIO.RISING, callback=note_b, bouncetime=200)
GPIO.add_event_detect(27, GPIO.RISING, callback=note_c, bouncetime=200)  
GPIO.add_event_detect(22, GPIO.RISING, callback=note_d, bouncetime=200)  
GPIO.add_event_detect(23, GPIO.RISING, callback=note_e, bouncetime=200)  
GPIO.add_event_detect(24, GPIO.RISING, callback=note_f, bouncetime=200)  

  
try:  
	print "Waiting for notes or stop with pin 25"  
	GPIO.wait_for_edge(25, GPIO.RISING)
	print "Pin 25 pressed - script end."  
  
except KeyboardInterrupt:  
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit 