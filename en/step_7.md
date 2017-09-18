## Playing sounds at the press of a button

- Have a look at the section below to see how a function can be called using a button push.

[[[rpi-python-function-calls-with-buttons]]]

- The function you want to call when the button is pressed is, for example, `drum.play()`.
- When you use a button to call a function, you don't need the `()`, you can just use `drum.play`.
- Now see if you can make your buttons trigger different sounds. Test and run your code to make sure all four buttons make sounds play. If something's not working, then have a look at the hints below.

--- hints --- --- hint ---
Earlier, you set up functions using the `pygame` module and called them in the shell by typing, for example, `drum.play()`. These function calls can be used by the `when_pressed` method.
--- /hint --- --- hint ---
To play the drum, you need a named button and the `drum` call. For example:
```python
btn_drum.when_pressed = drum.play
```
This should play the drum sound each time the button is pressed.
--- /hint --- --- hint ---
Here's a video showing how all the sounds can be triggered by pressing buttons. The buttons are wired to pins 4, 17, 27 and 10.
<video width="560" height="315" controls>
<source src="images/gpio-music-box-6.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
--- /hint --- --- /hints ---
