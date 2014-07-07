/*
	Sci Cen Music Box

	6 LEDs turn on and off in response to a pin number being 
        sent over I2C from RasPi (17, 18, 27, 22, 23, 24)

	The circuit:
	* Raspberry Pi Master over I2C
	* 6 LEDs

	Created 28 June 2014
	By Rachel Rayns
	Modified day month year
	By author's name

	https://github.com/RZRZR/sci-cen-music-box

*/

#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int data = 0;

int state[] = { 0, 0, 0, 0, 0, 0 };
int stateCount = 6;

int PiData[] = { 17, 18, 27, 22, 23, 24 };
int PiDataCount = 6;

int ledPins[] = { 2, 7, 6, 5, 4, 3 };
int ledPinsCount = 6;



void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);         // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);
    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    for (int thisPin = 0; thisPin < ledPinsCount; thisPin++)  {
      pinMode(ledPins[thisPin], OUTPUT);   
    Serial.println("Ready!");
    }
}
void loop() {
    delay(10);
}

// callback for received data
void receiveData(int byteCount){

    while(Wire.available()) {
        data = Wire.read();
        Serial.print("data received: ");
        Serial.println(data);
        
        for (int i = 0; int < PiDataCount; i++) {

          if (data == PiData[i]){
              
              if (state[i] == 0){
                  digitalWrite(ledPins[i], HIGH); // set the LED on
                  state[i] = 1;
              }
              else{
                  digitalWrite(ledPins[i], LOW); // set the LED off
                  state[i] = 0;
              }
           }
         
        }   

     }
}

// callback for sending data
void sendData(){
    Wire.write(data);
}
