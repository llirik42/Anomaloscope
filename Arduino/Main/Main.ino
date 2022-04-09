const int RED_LED_PIN = 6;
const int GREEN_LED_PIN = 9; 
const int YELLOW_LED_PIN = 3;

const int RED_POT_PIN = A2;
const int GREEN_POT_PIN = A0;

const int YELLOW_BRIGHTNESS = 255;
const int BAUD = 9600;
bool TO_PRINT_DATA = false;

int redValue;
int greenValue;


int GetRedBrightness(){
  return GetBrightness(analogRead(RED_POT_PIN));
}
int GetGreenBrightness(){
  return GetBrightness(analogRead(GREEN_POT_PIN));
}
int GetBrightness(int value){
  return map(value, 0, 1023, 0, 255); 
}

void PrintData(){
  Serial.print("red="); 
  Serial.print(redValue);
  Serial.print("   ");
  Serial.print("green=");
  Serial.print(greenValue);  
  Serial.println();
}

void SetPinModes(){
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(YELLOW_LED_PIN, OUTPUT);

  pinMode(RED_POT_PIN, INPUT);
  pinMode(GREEN_POT_PIN, INPUT);
}

void SetYellowLedBrightness(){
  analogWrite(YELLOW_LED_PIN, YELLOW_BRIGHTNESS);
}

void setup() {
  SetPinModes();

  SetYellowLedBrightness();
  
  Serial.begin(BAUD);
}

void loop() {  
  redValue = GetRedBrightness();
  greenValue = GetGreenBrightness();

  analogWrite(RED_LED_PIN, redValue);
  analogWrite(GREEN_LED_PIN, greenValue);

  if(TO_PRINT_DATA){
    PrintData();
  }
}
