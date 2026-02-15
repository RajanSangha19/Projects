#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// this code was based on the https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/  tutorial
// I would recommend using the code on that website as a test as well but this code should work fine
// There is also a wiring diagram also on the website 

// make sure to get all the libraries

RF24 radio(4, 5); // CE, CSN - set these pins yourself 

const byte address[6] = "00001"; // make sure that this address is this same on your reciever code 
int value = 0; // just a varaible that we will send to the reciever

void setup() {
  radio.begin(); // initialise 
  radio.openWritingPipe(address); 
  radio.setPALevel(RF24_PA_MAX); // set for maximum range
  radio.setDataRate(RF24_250KBPS);   
  radio.stopListening();
}

void loop() {
  int value = value + 1; 
  if (value == 1023){
    value  = 1;
  }
  radio.write(&value, sizeof(value));  // Sends 2 bytes only

  delay(5);  // Very fast transmission (200 packets/sec)
}
