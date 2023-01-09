#include <Servo.h>
Servo servo1; // creamos el objeto servo 1

String entradaSerial = ""; // variable string para almacenar entrada del otro programa 
bool entradaCompleta = false; // Indica si el strin está completo 

int servoPin = 9;
int pulsoMinimo = 580;
int pulsoMaximo = 2500;
int angulo = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(entradaSerial == "izq1/n"){
    Serial.print("0 grados/n"); // se manda por el puerto serial los grados que vamos a mover el servo xd
    servo1.write(0);
  }

  else if (entradaSerial == "izq2/n"){
    Serial.print("30 grados/n");
    servo1.write(30);
  }

  else if (entradaSerial == "izq3/n"){
    Serial.print("60 grados/n");
    servo1.write(60);
  }
  
  else if (entradaSerial == "ctr/n"){
    Serial.print("Centro 90 grados/n");
    servo1.write(90);
  }

  else if (entradaSerial == "der3/n"){
    Serial.print("120 grados/n");
    servo1.write(120);
  }

  else if (entradaSerial == "der2/n"){
    Serial.print("150 grados/n");
    servo1.write(150);
  }

  else if (entradaSerial == "der1/n"){
    Serial.print("180 grados/n");
    servo1.write(180);
  }

  else{ // Para cualquier otro dato ingresado 
    Serial.println("El dato recibido es invalido!");
  }

  entradaSerial = "";
  entradaCompleta = false;

}

void serialEvent() {
  while(Serial.available() ){
    // obtiene bytes de entrada
    char inChar = (char)Serial.read();
    // agrega al string de entrada
    entradaSerial +- inChar;

    if(inChar == '\n'){
      entradaCompleta = true;
    }
  }
















}
