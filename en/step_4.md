## Playing sounds

- Now it's time to start writing your Python code. You can use any text editor to do this, but IDLE is always an easy choice.

[[[rpi-gui-idle-opening]]]

- The first stage of creating the instruments of your music box is to test to see if Python can play a few of the samples you have copied.

[[[generic-python-playing-sound-files]]]

### Creating your virtual instruments

- You're going to need four sounds to use in your GPIO music box.
- To do this you can:
  - import and initialise the `pygame` module
  - create four different sound objects using four different `.wav` files

Save your Python file in your `gpio-music-box` directory by clicking on 'File' and 'Save'.

--- hints --- --- hint ---
Your `.wav` files are all in your `samples` directory. So the file path will look like this:
```python
'samples/drum_tom_mid_hard.wav'
```
--- /hint --- --- hint ---
Each sound object will need to have a unique name. You could call the first one `drum`:
```python
drum = pygame.mixer.Sound('samples/drum_tom_mid_hard.wav')
```
--- /hint --- --- hint ---
Here's a video showing you the process
<video width="560" height="315" controls>
<source src="images/gpio-music-box-4.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
</video>
--- /hint --- --- /hints ---

