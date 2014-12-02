# GPIO Music Box

Wire up a series of buttons that play particular sounds when pressed

## Getting started

First we'll create a Python program, import the GPIO and PyGame libraries and play a test sound file.

1. Boot your Pi and open LXTerminal from the Desktop.

1. Type the command `ls` and you should see the files and folders in your home directory.

1. There should be a folder called `music-box`. If this is not the case please follow the instructions in the [setup page](setup.md).

1. Enter the folder with `cd music-box`

1. Type `ls` and you shound see a `sounds folder`

1. Type `ls sounds` and you should see the example sound files.

1. Create a new Python file with `touch music-box.py`

1. Open the Python file in IDLE with the command `sudo idle music-box.py &`

    This opens IDLE, the Python application, with super user permissions as you'll need these to use GPIO.

    You'll see a Python prompt window (it will say some information about Python and then a new line starting with `>>>`, and another window which will be blank.

1. In the blank window, enter the following code to get started:

    ```python
    import pygame.mixer

    pygame.mixer.init()

    sound = pygame.mixer.Sound("sounds/note_a.wav")
    
    while True:
        sound.play()
    ```

    Here, we import the audio mixer module of the PyGame library and initialise it.

    Then we create a reference to one of the example sound files.

    The `while True` is a continuous loop containing a command to play the sound file. It will keep playing the sound repeatedly until the program is terminated.

1. Save the file with `Ctrl + S` and run with `F5`.

    It should play the sound repeatedly.
    
1. Click in to the Python prompt window and press `Ctrl + C` on the keyboard to force it to end.

    If you can't hear the sound, or it's coming out of the wrong speakers, you can change your audio configuration. Return to the terminal window and type the following command:

    ```bash
    amixer cset numid=3 2
    ```

    to switch audio to the headphone jack, or

    ```bash
    amixer cset numid=3 1
    ```

    to switch to HDMI.

    You only need to do this if your audio is coming out of the wrong speakers.

## Wire up first button

Now we've configured the audio and tested playing sound in Python, we'll connect the GPIO button.

1. Find a ground pin (marked `GND`) on the following diagram of the Raspberry Pi's pin layout:

    |-------:|:-------|
    |    3V3 | 5V     |
    |  GPIO2 | 5V     |
    |  GPIO3 | GND    |
    |  GPIO4 | GPIO14 |
    |    GND | GPIO15 |
    | GPIO17 | GPIO18 |
    | GPIO27 | GND    |
    | GPIO22 | GPIO23 |
    |    3V3 | GPIO24 |
    | GPIO10 | GND    |
    |  GPIO9 | GPIO25 |
    | GPIO11 | GPIO8  |
    |    GND | GPIO7  |
    |    DNC | DNC    |
    |  GPIO5 | GND    |
    |  GPIO6 | GPIO12 |
    | GPIO13 | GND    |
    | GPIO19 | GPIO16 |
    | GPIO26 | GPIO20 |
    |    GND | GPIO21 |

    Note that if you have an older Raspberry Pi model, you'll only have 26 pins but they are the same layout, starting from 
1. Attach a wire to a ground pin on the Raspberry Pi and connect it to the ground rail on your breadboard like so:

    ![](images/gpio-connect-ground.png)

1. Place the button on the breadboard and connect one of its feet to the ground rail.

1. Connect the button's other foot (on the same side) to GPIO pin 2 like so:

    ![](images/gpio-connect-pin2.png)

## Connect first button to sound file

Now we've connected a GPIO button, we'll make the sound play when the button is pressed.

1. Return to the code window and amend the code to add the GPIO library and set up pin 2 so it looks like this:

    ```python
    import pygame.mixer
    import RPi.GPIO as GPIO

    pygame.mixer.init()
    GPIO.modmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(2, GPIO.IN, GPIO.PUD_DOWN)

    sound = pygame.mixer.Sound("sounds/note_a.wav")
    ```

    This sets up GPIO pin 2 as an input, so you can trigger an event with the button.

1. Now add a function for playing the sound. This will be the code than runs when the button is pressed:

    ```python
    def play(pin):
        print("playing")
        sound.play()
    ```

    The `print` will tell you when the function has been called, so you know what's going on.

1. Create a GPIO event that will call the `play` function when the button is pressed:

    ```python
    GPIO.add_event_detect(2, GPIO.FALLING, play, 1000)
    ```

    The arguments passed to the function are:
    
    - the GPIO pin number (`2`)
    - the type of voltage change (`FALLING`)
    - the function to be used as the callback (`play`)
    - the amount of time allowed between button presses (`1000` milliseconds)

1. Add a line to print `ready` once it's all been set up and add a `while True` loop to wait for a button press:

    ```python
    print("ready")

    while True:
        pass
    ```

1. Run the program again and once you see `ready` printed to the screen, press the button and you should hear the sound played. Each time you press the button it should print `playing` to the screen and play the sound.

    If you do not see the word `playing` when you press the button, check you have it wired to the ground rail and pin 2 and that the cables are securely connected.

## Add second button with a different sound

Now that we've added an event for the button to trigger the sound to be played, we'll connect a second button and map that to a different sound.

1. Add a second button to the breadboard and wire it up to the ground rail and to GPIO pin 3 like so:

    ![](images/gpio-connect-pin3.png)

1. In the code, rename `sound` to `sound_a` and add a `sound_b` in the same way:

    ```python
    sound_a = pygame.mixer.Sound("sounds/note_a.wav")
    sound_b = pygame.mixer.Sound("sounds/note_b.wav")
    ```

1. We also need to perform the `GPIO.setup()` on pin 3 as well as pin 2. Rather than just copy this line, we'll automate the process.

    Normally we'd use a list like `pins = [2, 3, 4, 5]` and use a loop to run the setup for each item in the list. However as this time we also need a list of sounds that correspond to GPIO pins, we'll use another data structure called a *dictionary* which is used to store relationships between items.

1. After the `sound_b` line, create a dictionary mapping the two GPIO pins to their respective sounds, like so:

    ```python
    sound_pins = {
        2: sound_a,
        3: sound_b,
    }
    ```

    This means you can look up which sound to play by passing in the pin number, for example `sound_pins[2]` yields `sound_a` and `sound_pins[3]` yields `sound_b`.

    Now where we previously had the `GPIO.setup()` line for pin 2, we'll use a loop to set up all the pins in the `sound_pins` dictionary.

1. Use the following loop to set up each pin:

    ```python
    for pin in sound_pins:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
    ```

    Looping over a dictionary like this yields the dictionary keys (the left hand side) and passing a key in to a dictionary yields the corresponding value. For the pin setup all we need is the pin numbers.

    The other thing we want to do for each pin is set up the event detection.
    
    We *could* write a new function to play each particular sound, and add each event detection separately mapped to the appropriate function but it is possible to use a single function that determines which sound to play according to which pin was triggered.

1. Move the previously used `add_event_detect()` line in to this loop, replacing the hard-coded value of `2` for the loop variable `pin`:

    ```python
    for pin in sound_pins:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.FALLING, play, 1000)
    ```

    Now the `play` function will be called when pin `2` or `3` are triggered (by their connected buttons being pressed). However we need to amend the `play` function to make it play the right sound according to which button was pressed.

1. Amend the `play` function like so:

    ```python
    def play(pin):
        sound = sound_pins[pin]
        print("playing note from pin %s" % pin)
        sound.play()
    ```

    Because the event detection callback sends the GPIO pin number to the `play` function we can look it up in the `sound_pins` dictionary, set `sound` to the appropriate sound and then play it.

1. Now run the program again and when you see the ready message, try pressing each button. Different sounds should be played when each button is pressed.

## Connect more buttons

Now we've done all the hard work, it's really easy to connect more buttons to make more sounds!

For each extra button, all you need to do is:

1. Connect the button to the breadboard and wire it to the ground rail and another GPIO pin (make sure it's a pin marked GPIO in the pin diagram above).

1. Add a reference to the new sound file:

    ```python
    sound_c = pygame.mixer.Sound("sounds/note_c.wav")
    sound_d = pygame.mixer.Sound("sounds/note_d.wav")
    ```

1. Add the pin number and sound variable to the `sound_pins` dictionary:

    ```python
    sound_pins = {
        2: sound_a,
        3: sound_b,
        4: sound_c,
        14: sound_c,
    }
    ```

    And that's it! Re-run the program and the new buttons should make new sounds!

## What next?

Leaving the code as it is, you could make a presentation box with big colourful buttons that don't need a breadboard, and attach speakers to the side.

Try recording your own sounds and use them instead!
