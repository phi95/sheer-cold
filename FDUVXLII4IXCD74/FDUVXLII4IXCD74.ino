#include <max6675.h>


// ThermoCouple
int thermo_gnd_pin = 7;
int thermo_vcc_pin = 6;
int thermo_so_pin  = 5;
int thermo_cs_pin  = 4;
int thermo_sck_pin = 3;
String reader;
char c;
  
MAX6675 thermocouple(thermo_sck_pin, thermo_cs_pin, thermo_so_pin);
  
void setup() {
  Serial.begin(9600);

  pinMode(thermo_vcc_pin, OUTPUT); 
  pinMode(thermo_gnd_pin, OUTPUT); 
  digitalWrite(thermo_vcc_pin, HIGH);
  digitalWrite(thermo_gnd_pin, LOW);
}

void loop() {
  
  while (Serial.available()){
    if (Serial.available() > 0){
      c = Serial.read();
      reader += c;
      //Serial.println(reader + "&");
    };
  }
  if (reader.length() > 0){
    Serial.println(reader + "&");
    reader = "";
  };
  
  Serial.println(thermocouple.readCelsius()-5);
  delay(1000);
}
