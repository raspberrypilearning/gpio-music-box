## Improving your script

The code you have written should work without any problems. However, it's generally a good idea to make your code a little cleaner once you have a working prototype.

The next steps are completely optional. If you're happy with your script, then just leave it as it is. If you want to make it a little cleaner, then have a go.

You can store your button objects and sounds in a dictionary, instead of having to create eight different objects.

Have a look at the steps below to learn about creating basic dictionaries and then looping over them.

[[[generic-python-basic-dictionaries]]]
[[[generic-python-iterating-dictionaries]]]

--- task ---
Firstly you want to create a dictionary that uses the `Button`s as keys and the `Sound`s as values.

```python3
button_sounds = {Button(4): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav"),
                 Button(17): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav"),
                 Button(27): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav"),
                 Button(10): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")}
```
--- /task ---

[[[generic-python-functions-in-dictionaries]]]

--- task ---
You can now loop over the dictionary to tell the program to play the sound when the button is pressed.
```python
for button, sound in button_sounds.items():
    button.when_pressed = sound.play
```
--- /task ---

--- collapse ---
---
title: Your full code should now look like this:
---
```python
import pygame
from gpiozero import Button

pygame.init()

button_sounds = {Button(4): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav"),
                 Button(17): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav"),
                 Button(27): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav"),
                 Button(10): pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play
```
--- /collapse ---



