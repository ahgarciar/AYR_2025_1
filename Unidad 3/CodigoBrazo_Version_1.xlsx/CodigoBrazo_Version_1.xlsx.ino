int inputs[] = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31};
//22, 23 -> motor 1 -: Cadera
//24, 25 -> motor 2 -: Hombro
//26, 27 -> motor 3 -: Codo
//28, 29 -> motor 4 -: Muñeca 1
//30, 31 -> motor 5 -: Muñeca 2

int enables[] = {49, 50, 51, 52, 53};
//49 -> motor 1
//50 -> motor 2
//51 -> motor 3
//52 -> motor 4
//53 -> motor 5

void setup() {
  // put your setup code here, to run once:
  //Modo de trabajo
for(int i=0;i<10;i++){
  pinMode(inputs[i], OUTPUT);
}
for(int i=0; i<5;i++){
  pinMode(enables[i], OUTPUT);
}

Serial.begin(9600);
Serial.setTimeout(100);
//1-1 :--- motor 1 sentido avanzar.  ----
//1-0 :--- motor 1 sentido retroceder .---

}

void estableceSentidoMotor(int motor, int sentido){
  switch(motor){
    case 0:
        digitalWrite(enables[0], 1);
        if(sentido==1){
            digitalWrite(inputs[0], 1);
            digitalWrite(inputs[1], 0);
        }
        else{
            digitalWrite(inputs[0], 0);
            digitalWrite(inputs[1], 1);
        }
      break;
    case 1:
      digitalWrite(enables[1], 1);

      if(sentido==1){
          digitalWrite(inputs[2], 1);
          digitalWrite(inputs[3], 0);
        }
        else{
          digitalWrite(inputs[2], 0);
          digitalWrite(inputs[3], 1);
        }
      break;
    case 2:
      digitalWrite(enables[2], 1);
      if(sentido==1){
          
          digitalWrite(inputs[4], 1);
          digitalWrite(inputs[5], 0);
        }
        else{

          digitalWrite(inputs[4], 0);
          digitalWrite(inputs[5], 1);
        }
      break;
    case 3:
      digitalWrite(enables[3], 1);
      if(sentido==1){
          
          digitalWrite(inputs[6], 1);
          digitalWrite(inputs[7], 0);
        }
        else{

          digitalWrite(inputs[6], 0);
          digitalWrite(inputs[7], 1);
        }
      break;
    case 4:
      digitalWrite(enables[4], 1);
      if(sentido==1){
          
          digitalWrite(inputs[8], 1);
          digitalWrite(inputs[9], 0);
        }
        else{

          digitalWrite(inputs[8], 0);
          digitalWrite(inputs[9], 1);
        }
      break;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String cadena = Serial.readString();
    int motor = String(cadena.charAt(0)).toInt();
    int sentido = String(cadena.charAt(2)).toInt();
    Serial.println(String(motor) + "---" + String(sentido));
    estableceSentidoMotor(motor, sentido);
  }
  delay(100);
}
