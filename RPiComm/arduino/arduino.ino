#define CLK_PIN 3
#define DATA_PIN 4

bool byteArr[8] = {false};
int curBit = 0;
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

  byte character = 0;
  for(int i = 7; i >= 0; i--)
  {
    if(byteArr[i])
    {
      character |= (1 << (7-i));
    }
  }

  Serial.print((char)character);
}

void setBitArr(){
  byteArr[curBit] = bitState;
  curBit++;
  if(curBit == 8)
  {
    curBit = 0;
    printChar();
  }
 }

void interrupt(){
  if(digitalRead(DATA_PIN) == HIGH)
  {
    Serial.print("1");
    bitState = true;
  }
  else
  {
    Serial.print("0");
    bitState = false;
  }
  setBitArr();
}



