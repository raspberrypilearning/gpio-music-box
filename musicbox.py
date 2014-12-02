import pygame.mixer
import RPi.GPIO as GPIO

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sound_a = pygame.mixer.Sound("sounds/note_a.wav")
sound_b = pygame.mixer.Sound("sounds/note_b.wav")
sound_c = pygame.mixer.Sound("sounds/note_c.wav")
sound_d = pygame.mixer.Sound("sounds/note_d.wav")
sound_e = pygame.mixer.Sound("sounds/note_e.wav")
sound_f = pygame.mixer.Sound("sounds/note_f.wav")

sound_pins = {
    2: sound_a,
    3: sound_b,
    4: sound_c,
    14: sound_d,
    15: sound_e,
    17: sound_f,
}

def play(pin):
    sound = sound_pins[pin]
    sound.play()
    print("playing note from pin %s" % pin)

def main():
    for pin in sound_pins:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.FALLING, play, 1000)

    print("waiting for button press")

if __name__ == "__main__":
    main()
