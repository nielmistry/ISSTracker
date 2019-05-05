#include <LiquidCrystal.h>
#include "ShiftReg.h"

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

boolean horizon = false;

const uint8_t SOM_CODE[4] = {0x7f, 0xff, 0x00, 0x00};
const uint8_t EOM_CODE[4] = {0x7f, 0xff, 0xff, 0xff};
const int IN_MSG_BUF_SIZE = 30;

/* MSG FORMAT: {SOM1, SOM2, SOM3, SOM4, MSG_CODE, PAY1, ..., PAYN, EOM1, EOM2, EOM3, EOM4} */
uint8_t in_msg_buf[IN_MSG_BUF_SIZE];
int in_msg_ptr = 0;

ShiftReg interpreter_buf;

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
  getSerial();

  dtostrf(alt.f,3,3,alt_c);
  dtostrf(az.f,3,3,az_c);
  lcd.setCursor(6,0);
  lcd.write(alt_c);
  lcd.setCursor(6,1);
  lcd.write(az_c);

  delay(500);
  
}

void getSerial()
{
  while(Serial.available())
  {
    uint8_t byte_in = Serial.read();
    in_msg_buf[in_msg_ptr] = byte_in;
    in_msg_ptr++;

    interpreter_buf.input(byte_in);

    if(interpreter_buf.validate(EOM_CODE))
    {
      interpretMessage();
    }

    if(in_msg_ptr >= IN_MSG_BUF_SIZE)
    {
      in_msg_ptr = 0;
      interpreter_buf.flush();
    }
  }
}

void interpretMessage()
{
  uint8_t msg_code = 0x00;
  uint8_t msg_start_loc = 0;

  interpreter_buf.flush();
  for(int i = 0; i < IN_MSG_BUF_SIZE - 5; i++) // no point if msg is too small
  {
    // find SOM
    interpreter_buf.input(in_msg_buf[i]);
    if(interpreter_buf.validate(EOM_CODE, true));
    {
      msg_code = in_msg_buf[i + 1];
      msg_start_loc = i + 2;
      break;
    }
  }

  switch(msg_code)
  {
    case 0xaa:
      for(int i = 0; i < 4; i++)
      {
        alt.buf[i] = in_msg_buf[msg_start_loc + i];
      }
      break;
    case 0xab:
      for(int i = 0; i < 4; i++)
      {
        az.buf[i] = in_msg_buf[msg_start_loc + i];
      }
      break;
    case 0xbb:
      for(int i = 0; i < 4; i++)
      {
        alt.buf[i] = in_msg_buf[msg_start_loc + i];
      }
      for(int i = 0; i < 4; i++)
      {
        az.buf[i] = in_msg_buf[msg_start_loc + i];
      }
      break;
  }
  
  interpreter_buf.flush();
  in_msg_ptr = 0;
}

