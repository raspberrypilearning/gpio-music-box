## Playing sounds at the press of a button

You can have a look at the section below to see how a function can be called using a button push.

[[[rpi-python-function-calls-with-buttons]]]

The function you want to call when the button is pressed is, for example, `drum.play()`.

However, when using an event, such as a button push, to call a function, you don't use the brackets `()`.

This is because you don't want the function to be called straight away, but rather be called only when the button is pushed. So in this case you just use `drum.play`.

--- task ---
First set up one of your buttons, remembering to use the numbers for the pins **you** have used.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
highlight_lines: 2, 11
---
import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
bell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")

btn_drum = Button(4)
--- /code ---
--- /task ---

--- task ---
To play the sound when the button is pushed, just add this line of code to the bottom of your file:

```python
btn_drum.when_pressed = drum.play
```
--- /task ---

--- task ---
Run the program and push the button. If you don't hear the sound playing, then check the wiring of your button.
--- /task ---

--- task ---
Now add code to make the remaining three buttons play their sounds.

--- hints --- --- hint ---
You can start by adding a `btn_cymbal` for instance, and linking it to the `cymbal.play()` function.
--- /hint --- --- hint ---
Here's an example of getting a second button working

```python
btn_cymbal = Button(17)

btn_cymbal.when_pressed = cymbal.play
```
--- /hint --- --- /hints ---

--- collapse ---
---
title: Here's what your full code should look like:
---
```python
import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
bell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")

btn_drum = Button(4)
btn_cymbal = Button(17)
btn_snare= Button(27)
btn_bell = Button(10)

btn_drum.when_pressed = drum.play
btn_cymbal.when_pressed = cymbal.play
btn_snare.when_pressed = snare.play
btn_bell.when_pressed = bell.play
```
--- /collapse ---


