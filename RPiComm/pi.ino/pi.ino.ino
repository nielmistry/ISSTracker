#define CLK_PIN 3
#define DATA_PIN 4

bool byteArr[8] = {false};
int curBit = 0;
//byte charByte = 0;
volatile bool bitState = false;
  
void setup() {
  // put your setup code here, to run once:
  pinMode(CLK_PIN, INPUT);
  pinMode(DATA_PIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(CLK_PIN), interrupt, RISING);
  Serial.begin(9600);
}

void loop() {

}

void printChar()
{
  byte charByte = 0;
  for(int i = 0; i < 8; i++)
  {
    if(byteArr[i])
    {
      Serial.print("1");
//      charByte = charByte | (1 << i);
    }
    else
    {
      Serial.print("0");
    }
  }
//  Serial.print('\n');
//  Serial.print(charByte);
}

void setBitArr(){
//  if(bitState)
//  {
//    charByte |= (1 << curBit);
//  }
  byteArr[curBit] = bitState;
  curBit++;
  if(curBit == 8)
  {
    curBit = 0;
//    Serial.print(char(charByte)); 
    printChar();
    Serial.print("\n");
//    charByte = 0;
  }
 }

void interrupt(){
  if(digitalRead(DATA_PIN) == HIGH)
  {
//    Serial.print("1");
    bitState = true;
  }
  else
  {
//    Serial.print("0");
    bitState = false;
  }
  setBitArr();
}



