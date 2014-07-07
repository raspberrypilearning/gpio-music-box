#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int data = 0;

int state1 = 0;
int state2 = 0;
int state3 = 0;
int state4 = 0;
int state5 = 0;
int state6 = 0;

int led1 = 2;
int led2 = 7;
int led3 = 4;
int led4 = 6;
int led5 = 5;
int led6 = 3;

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);         // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);

    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    Serial.println("Ready!");
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

        if (data == 17 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state1 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state1 = 0;
            }
         }
         
         if (data == 18 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state2 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state2 = 0;
            }
         }
         
         if (data == 27 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state3 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state3 = 0;
            }
         }

         if (data == 22 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state4 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state4 = 0;
            }
         }

         if (data == 23 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state5 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state5 = 0;
            }
         }

         if (data == 24 ){

            if (state == 0){
                digitalWrite(led1, HIGH); // set the LED on
                state6 = 1;
            }
            else{
                digitalWrite(led1, LOW); // set the LED off
                state6 = 0;
            }
         }

     }
}

// callback for sending data
void sendData(){
    Wire.write(data);
}
