#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// this code was based on the https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/  tutorial
// I would recommend using the code on that website as a test as well but this code should work fine
// There is also a wiring diagram also on the website 

RF24 radio(4, 5); // CE, CSN - set these yourself

const byte address[6] = "00001";

void setup() {
  Serial.begin(115200);  
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MAX);
  radio.setDataRate(RF24_250KBPS);   // must match transmitter
  radio.startListening();
}

void loop() {
  if (radio.available()) {

    int receivedValue;   // Must match transmitter type

    radio.read(&receivedValue, sizeof(receivedValue));

    Serial.println(receivedValue);
  }
}
