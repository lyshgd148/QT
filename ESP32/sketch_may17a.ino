
const int Pin = 2;
unsigned long startTime;
unsigned long endTime;
unsigned long Duration;

void setup() {
  pinMode(Pin, INPUT);
  Serial.begin(9600);

}

void loop() {

  while (digitalRead(Pin) == LOW) {}
  startTime = micros();
  while (digitalRead(Pin) == HIGH) {}
  endTime = micros();
  Duration = endTime - startTime;
  if (50<=Duration&&Duration<=450) Serial.write(0);
  else if (300<=Duration&&Duration<=700) Serial.write(1);

}