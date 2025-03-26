int i;

void setup() {
  // put your setup code here, to run once:
  i = 0;
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola" + String(i++));
  delay(250);
}
