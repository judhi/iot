// Arduino / ESP32 sketch
// for sending random generated data to Serial Port
// by Judhi Prasetyo 2020
void setup() {
  Serial.begin(9600);  // start serial communication at this speed
}
void loop() {
  int r = random(100);  // generate random number up to 100
  Serial.print(r);      // send the number to Serial port
  Serial.println();     // send New Line to Serial port
  delay(3000);          // wait for 3 sec
}
