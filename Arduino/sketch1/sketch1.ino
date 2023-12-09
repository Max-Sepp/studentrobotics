#define FL // Pin for front left motor
#define FR // Pin for front right motor
#define BL // etc
#define BR // etc

// KES, 2023/2024

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}

void writePins(int[] pins, int[] values) {
  for (i = 0; i < sizeof(pins)/sizeof(pins[0]); i++) {
    digitalWrite(pins[i], values[i])
  }
}
