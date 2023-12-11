/* Example sketch to control a stepper motor with TB6600 stepper motor driver 
  and Arduino without a library: continuous rotation. 
  More info: https://www.makerguides.com */

// Define stepper motor connections:
#define dirFRPin 2
#define stepFRPin 3

#define dirFLPin 4
#define stepFLPin 5

#define dirBRPin 6
#define stepBRPin 7

#define dirBLPin 8
#define stepBLPin 9

int sensorPin = A0;   // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  Serial.begin(9600);

  // Declare pins as output:
  pinMode(stepFRPin, OUTPUT);
  pinMode(dirFRPin, OUTPUT);

  pinMode(stepFLPin, OUTPUT);
  pinMode(dirFLPin, OUTPUT);

  pinMode(stepBRPin, OUTPUT);
  pinMode(dirBRPin, OUTPUT);

  pinMode(stepBLPin, OUTPUT);
  pinMode(dirBLPin, OUTPUT);

  digitalWrite(dirFRPin, LOW);
  digitalWrite(dirFLPin, HIGH);
  digitalWrite(dirBRPin, LOW);
  digitalWrite(dirBLPin, LOW);

}

void loop() {
  // These four lines result in 1 step:
  digitalWrite(stepFRPin, HIGH);
  digitalWrite(stepFLPin, HIGH);
  digitalWrite(stepBRPin, HIGH);
  digitalWrite(stepBLPin, HIGH);

  delayMicroseconds(500);

  digitalWrite(stepFRPin, LOW);
  digitalWrite(stepFLPin, LOW);
  digitalWrite(stepBRPin, LOW);
  digitalWrite(stepBLPin, LOW);

  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  
  Serial.println(sensorValue);

  delayMicroseconds(sensorValue * 0.488);
}
