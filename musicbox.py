import RPi.GPIO as GPIO
import pygame.mixer

pygame.mixer.init(44000, -16, 2, 500)
GPIO.setmode(GPIO.BCM)

# Pin 25 stops the script
GPIO.setup(25, GPIO.IN, GPIO.PUD_DOWN)

sound_a = pygame.mixer.Sound("sounds/note_a.wav")
sound_b = pygame.mixer.Sound("sounds/note_b.wav")
sound_c = pygame.mixer.Sound("sounds/note_c.wav")
sound_d = pygame.mixer.Sound("sounds/note_d.wav")
sound_e = pygame.mixer.Sound("sounds/note_e.wav")
sound_f = pygame.mixer.Sound("sounds/note_f.wav")

sound_pins = {
    17: sound_a,
    18: sound_b,
    27: sound_c,
    22: sound_d,
    23: sound_e,
    24: sound_f,
}

def setup_pin(pin):
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

def play(pin):
    sound = sound_pins[pin]
    sound.play()
    print("Playing note %s" % pin)

def main():
    for pin in sound_pins:
        setup_pin(pin)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=play, bouncetime=1000)

    print("Waiting for Pin 25 to end script")
    GPIO.wait_for_edge(25, GPIO.RISING)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
