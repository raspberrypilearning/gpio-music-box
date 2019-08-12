## Connecting your buttons

You're going to need four buttons, each wired to separate GPIO pins on the Raspberry Pi.

[[[rpi-gpio-pins]]]

[[[rpi-gpio-wiring-a-button]]]

--- task ---
Place your four buttons into your breadboard.
--- /task ---

--- task ---
Wire each button up to a different numbered GPIO pin. You can choose any pins you like, but you will need to remember their numbers.
--- /task ---


--- hints --- --- hint ---
You can wire a single **GND** pin to the negative *blue* rail on the breadboard. Then wire one leg of each button to this rail. The remaining legs of the buttons can be wired to individual GPIO pins.
--- /hint --- --- hint ---

--- /hint --- --- hint ---
Here's a wiring diagram that might help using pins `4`, `17`, `27` and `10`
![4-btn](images/4-btn.png)
Here's a video showing how the buttons can be wired.
<video width="560" height="315" controls>
<source src="images/gpio-music-box-5.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
--- /hint --- --- /hints ---



