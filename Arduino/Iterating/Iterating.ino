#include <ColorLib.h>
#include <ColorSensorLib.h>


const Sensor ColorSensor = Sensor(1, 2, 3, 4, 5, 6, 20); // (s0, s1, s2, s3, led, out, freq)
const Color TARGET_COLOR = Color(7, 32, 0);
const int RED_LED_PIN = 7;
const int GREEN_LED_PIN = 8;

const int NUMBER_OF_CASES_FOR_EACH_COLOR = 11;
const int NUMBER_OF_DIGITS_AFTER_POINT = 1;
const int BAUD = 9600;


void PrintSettings(){  
  Serial.print(sq(NUMBER_OF_CASES_FOR_EACH_COLOR));
  Serial.print(' ');
  Serial.println(TARGET_COLOR.GetRedAndGreenRepr());
}

void PrintData(float red, float green, Color sensorColor){    
  Serial.print(red, NUMBER_OF_DIGITS_AFTER_POINT);
  Serial.print(' ');
  Serial.print(green, NUMBER_OF_DIGITS_AFTER_POINT);
  Serial.print(' ');
  Serial.println(sensorColor.GetRedAndGreenRepr());
  
  return 0;
}

void SetBrightness(float red, float green){  
  analogWrite(RED_LED_PIN, int(red * 255));
  analogWrite(GREEN_LED_PIN, int(green * 255));
}

void DoIterating(){
  const float accuracy = 1.0 / (NUMBER_OF_CASES_FOR_EACH_COLOR - 1);
    
  float red = 0, green = 0;

  Color currentColor;

  for(int redCounter = 0; redCounter < NUMBER_OF_CASES_FOR_EACH_COLOR; redCounter++){
    green = 0;
    
    for(int greenCounter = 0; greenCounter < NUMBER_OF_CASES_FOR_EACH_COLOR; greenCounter++){
      SetBrightness(red, green);
      
      currentColor = ColorSensor.GetSensorColor();
    
      PrintData(red, green, currentColor);

      green += accuracy;
    }

    red += accuracy;   
  }
}

void setup() {
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);

  Serial.begin(BAUD);

  PrintSettings();

  DoIterating();
}

void loop() {}
