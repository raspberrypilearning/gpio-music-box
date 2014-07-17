/* 
Sci Cen Music Box 

6 LEDs turn on and off in response to a pin number being 
sent over I2C from RasPi (17, 18, 27, 22, 23, 24) 

The circuit: 
* Raspberry Pi Master over I2C 
* 6 LEDs 

Created 28 June 2014 
By Rachel Rayns 
Modified 4 July 2014 
By Ashley Brown (@arctic_sunrise)

https://github.com/RZRZR/sci-cen-music-box 

*/ 

#include <Wire.h> 

#define SLAVE_ADDRESS 0x04 

int data = 0; 

int state[] = { 0, 0, 0, 0, 0, 0 }; 
int stateCount = 6; 

int PiData[] = { 17, 18, 27, 22, 23, 24 }; 
int PiDataCount = 6; 

int ledPins[] = { 8, 9, 10, 11, 12, 13 };  
int ledPinsCount = 6; 



void setup() { 
pinMode(13, OUTPUT); 
Serial.begin(9600); // start serial for output 
// initialize i2c as slave 
Wire.begin(SLAVE_ADDRESS); 
// define callbacks for i2c communication 
Wire.onReceive(receiveData); 
Wire.onRequest(sendData); 

for (int thisPin = 0; thisPin < ledPinsCount; thisPin++) { 
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




int arrayLength = stateCount; 


for (int counter = 0; counter < arrayLength; counter++) { 

if (data = PiData[counter]) { 

//read the data and does it match the first pos in the array - if not then it just iterates to the next one 


int stateChoice = state[counter]; 

switch (stateChoice) { 
case 0: 
digitalWrite(ledPins[counter], HIGH); // set the LED on 
state[counter] =1;	
break; 
case 1: 
digitalWrite(ledPins[counter], LOW); // set the LED off 
state[counter] = 0; 
break; 


}//end switch 


}//endif 

}//endfor 

} 
} 

// callback for sending data 
void sendData(){ 
Wire.write(data); 
} 
