## Improving your script

The code you have written should work without any problems. However, it's generally a good idea to make your code a little cleaner once you have a working prototype. The next steps are completely optional. If you're happy with your script, then just leave it as it is. If you want to make it a little cleaner, then try the following challenge.

- You can store your button objects and sounds in a dictionary, instead of having to create eight different objects.

- Have a look at the steps below to learn about creating basic dictionaries and then looping over them.

[[[generic-python-basic-dictionaries]]]
[[[generic-python-iterating-dictionaries]]]

- Can you create a dictionary that contains your `Button()` objects as keys and your `Sound()` objects as values?

[[[generic-python-functions-in-dictionaries]]]

- If you have a dictionary of `Button()` and `Sound()` objects, you can now loop over them with a `for` loop, so that each button is tied to a different sound.

--- hints --- --- hint ---
Your dictionary should contain the button objects linked to the sounds to be played. For instance, your first key:value pair might look like this:

```python
button_sounds = {Button(2): Sound("samples/drum_tom_mid_hard.wav")}
```

--- /hint --- --- hint ---
You can iterate over the dictionary to link each button to its sound.
```python
for button, sound in button_sounds.items():
    button.when_pressed = sound.play
```
--- /hint --- --- hint ---
Here's a video showing how the code can be written:
<video width="560" height="315" controls>
<source src="images/gpio-music-box-7.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
--- /hint --- --- /hints ---
