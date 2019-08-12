## Playing sounds at the press of a button

You can have a look at the section below to see how a function can be called using a button push.

[[[rpi-python-function-calls-with-buttons]]]

The function you want to call when the button is pressed is, for example, `drum.play()`.

However, when using an event, such as a button push, to call a function, you don't use the brackets `()`.

This is because you don't want the function to be called straight away, but rather be called only when the button is pushed. So in this case you just use `drum.play`.

