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
  for(int i = 0; i < 8; i++)
  {
    if(byteArr[i])
    {
      Serial.print("1");
    }
    else
    {
      Serial.print("0");
    }
  }
}

void setBitArr(){
  byteArr[curBit] = bitState;
  curBit++;
  if(curBit == 8)
  {
    curBit = 0;
//    printChar();
    Serial.print("\n");
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



