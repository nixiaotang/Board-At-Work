#include <Stepper.h>

//Both motors move clockwise -> top right to bottom left
//Both motors move counterclockwise -> bottom left to top right due to power imbalance

//MECHANICS: inwards -> down, outwards -> up, both CCW -> right, both CW -> left

#define dirPin 2
#define stepPin 3
#define stepsPerRevolution 200
#define LED 8

#define dirPin2 8 
#define stepPin2 9

Stepper myStepper1 (stepsPerRevolution, dirPin, stepPin); //this guy moves CW for +1, CCW for -1
Stepper myStepper2 (stepsPerRevolution, dirPin2, stepPin2); //this guy moves CW for +1, CCW for -1

void setup() {

  myStepper1.setSpeed(100);
  myStepper2.setSpeed(100);
  Serial.begin(9600);
}

void loop() {
  
 //for (int i=0; i<=800; i++){
  myStepper1.step(+1); // both 1 makes them both move clockwise, moving the carriage top right to bottom left
  myStepper2.step(-1); //
 //}
 
 
}