#pragma once

class Color{
  int red;
  int green;
  int blue;
 
public:
  Color(int Red, int Green, int Blue){ 
    red = Red;
    green = Green;
    blue = Blue;
  }
  Color(){}
        
  String GetRedAndGreenRepr(){    
    return (String)red + " " + (String)green;
  } 
};