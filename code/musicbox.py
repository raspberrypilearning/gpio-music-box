import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2): Sound("samples/drum_tom_mid_hard.wav"),
    Button(3): Sound("samples/drum_cymbal_open.wav"),
    Button(4): Sound("samples/elec_bell.wav"),
    Button(14): Sound("samples/elec_hi_snare.wav"),
}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play

pause()
