#include <Servo.h>

byte pos;
Servo servo;
boolean received  = false;

void setup() {
    servo.attach(9);
    Serial.begin(115200);
    servo.write(90);
}

void loop() {
    while(Serial.available() > 0) {
        pos = (byte)Serial.read();
        received = true;
    }

    if(received) {
        servo.write(pos);
        received = false;
    }

    delay(10);
}
