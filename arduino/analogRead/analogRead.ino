#define ANALOG_PIN A0

void setup() {
  pinMode(ANALOG_PIN, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(ANALOG_PIN));
}
