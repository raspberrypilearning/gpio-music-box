Science Centre - Music Box
=================

#### New install of Raspian



#### Configure I2C

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

update ```musicbox.py``` and ```ledsketch``` with correct i2c address

#### Wiring

##### Raspberry Pi:

**Inputs (expecting 3.3V):**

GPIO 17

GPIO 18

GPIO 27

GPIO 22

GPIO 23

GPIO 24

**Speaker:**

Either 3.5mm jack or USB + 3.5mm jack Adafruit Audio Card.

##### Arduino:

**LEDs should go from PIN to LED to GND, using appropriate resistors.**

PIN 8

PIN 9

PIN 10

PIN 11

PIN 12

PIN 13

##### i2c (connecting the RasPi and Arduino):

Raspberry Pi | Arduino|
-----  		 | ------- |
GPIO 0 (SDA)| Pin 4 (SDA)|
GPIO 1 (SCL)| Pin 5 (SCL)|
GND| GND|







#### Install Adafruit Audio Card (if using USB sound card)

https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/cm108-type
