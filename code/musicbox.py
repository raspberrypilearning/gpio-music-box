import pygame.mixer
import RPi.GPIO as GPIO
import signal

pygame.mixer.init()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

drum = pygame.mixer.Sound("samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("samples/drum_cymbal_open.wav")
bell = pygame.mixer.Sound("sounds/elec_bell.wav")
snare = pygame.mixer.Sound("sounds/elec_hi_snare.wav")

sound_pins = {
    2: drum,
    3: cymbal,
    4: bell,
    14: snare,
}

def play(pin):
    sound = sound_pins[pin]
    print("playing note from pin %s" % pin)
    sound.play()

for pin in sound_pins:
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.FALLING, play, 100)

print("ready")

while True:
    signal.pause()
    pass
