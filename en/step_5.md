## Play sounds at the press of a button

To see how a function can be called using a button press, have a look at the section below.

[[[rpi-python-function-calls-with-buttons]]]

When the button is pressed, the program should call a function such as `drum.play()`.

However, when you use an event (such as a button press) to call a function, you don't use brackets `()`.

This is because the program must only call the function when the button is pressed, rather than straight away. So, in this case, you just use `drum.play`.

--- task ---

First, set up one of your buttons. Remember to use the numbers for the GPIO pins that **you** have used, rather than the numbers in the example.

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

drum = pygame.mixer.Sound("drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("drum_snare_hard.wav")
bell = pygame.mixer.Sound("drum_cowbell.wav")

btn_drum = Button(4)
--- /code ---

--- /task ---

--- task ---

To play the sound when the button is pressed, just add this line of code to the bottom of your file:

```python
btn_drum.when_pressed = drum.play
```
--- /task ---

--- task ---

Run the program and press the button. If you don't hear the sound playing, then check the wiring of your button.

--- /task ---

--- task ---

Now, add code to make the remaining three buttons play their sounds.

--- hints --- --- hint ---

For example, you could add a `btn_cymbal`, and link it to the `cymbal.play()` function.

--- /hint --- --- hint ---

Here's an example of the code that you could use for a second button.

```python
btn_cymbal = Button(17)

btn_cymbal.when_pressed = cymbal.play
```

--- /hint --- --- /hints ---

--- /task ---

--- collapse ---
---
title: Full code listing
---
```python
import pygame
from gpiozero import Button

pygame.init()

drum = pygame.mixer.Sound("drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("drum_snare_hard.wav")
bell = pygame.mixer.Sound("drum_cowbell.wav")

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
