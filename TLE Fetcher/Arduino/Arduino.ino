#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

boolean horizon = false;

char alt_c[10];
char az_c[10]; 

union {
  uint8_t buf[4];
  float f;
} alt;

union {
  uint8_t buf[4];
  float f;
} az;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  
  lcd.begin(16, 2);
  lcd.write("Alt: ");
  lcd.setCursor(0,1);
  lcd.write("Az: ");

}

void loop() {
  if(Serial.available())
  {
    // read 4 bytes
    for(int i = 0; i < 4; i++)
    {
      alt.buf[i] = Serial.read();  
    }
  }
  dtostrf(alt.f,3,3,alt_c);
  dtostrf(az.f,3,3,az_c);
  lcd.setCursor(6,0);
  lcd.write(alt_c);
  lcd.setCursor(6,1);
  lcd.write(az_c);

  while(Serial.available())
  {
    Serial.read();
  }
  delay(500);
  
}
