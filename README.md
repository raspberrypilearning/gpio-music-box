Science Centre - Music Box
=================

Raspian. update RPi.GPIO.

``` wget http://raspberry-gpio-python.googlecode.com/files/python-rpi.gpio_0.5.1a-1_armhf.deb ```

``` wget http://raspberry-gpio-python.googlecode.com/files/python3-rpi.gpio_0.5.1a-1_armhf.deb ```

``` sudo dpkg -i python-rpi.gpio_0.5.1a-1_armhf.deb ```

``` sudo dpkg -i python3-rpi.gpio_0.5.1a-1_armhf.deb ```

Install audio

``` sudo apt-get install alsa-utils ``` 

``` sudo apt-get install mpg321 ``` 


Install Adafruit Audio Card.

https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/cm108-type


Make ex.

``` chmod +x musicbox.py ``` 

``` sudo python musicbox.py ``` 