#pragma once
#include <Arduino.h>
#include <ColorLib.h>

class Sensor{
	int s0;
	int s1;
	int s2;
	int s3;
	int led;
	int out;
 
	void SetPinModes(){
		pinMode(s0, OUTPUT);
  		pinMode(s1, OUTPUT);
  		pinMode(s2, OUTPUT);
  		pinMode(s3, OUTPUT);
  		pinMode(out, INPUT);
  		pinMode(led, OUTPUT);
  	}

  	
	void SetFrequency(int freq){
		if(freq == 2){
			digitalWrite(s0, LOW);
  			digitalWrite(s1, HIGH);
		}
		else if(freq == 100){
			digitalWrite(s0, HIGH);
  			digitalWrite(s1, HIGH);
		}
		else{
			digitalWrite(s0, HIGH);
  			digitalWrite(s1, LOW);
		}
	}
	
	void SetLedMode(){
		if(led != -1){
			digitalWrite(led, LOW);
		}
	}


public:
	Sensor(int S0, int S1, int S2, int S3, int LED, int OUT, int freq){ 
		s0 = S0;
    	s1 = S1;
    	s2 = S2;
    	s3 = S3;
    	led = LED;
    	out = OUT;

		SetPinModes();

		SetFrequency(freq);

		SetLedMode();
  	}

  	Color GetSensorColor(){
  		digitalWrite(s2, LOW);
  		digitalWrite(s3, LOW);
  		int red = pulseIn(out, LOW);

  		digitalWrite(s2,HIGH);
  		digitalWrite(s3,HIGH);
  		int green = pulseIn(out, LOW);
  
  		Color result = Color(red, green, 0);

  		return result;
	}
};