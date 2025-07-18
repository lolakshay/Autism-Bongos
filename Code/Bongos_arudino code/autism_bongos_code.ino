// FSR analog input pins
const int fsr1Pin = A0; // LEFT
const int fsr2Pin = A1; // RIGHT

// Relay output pins
const int relay1Pin = 7;
const int relay2Pin = 8;

// Thresholds (adjust as needed)
const int threshold1 = 200; // For FSR 1 (LEFT)
const int threshold2 = 200; // For FSR 2 (RIGHT)

void setup() {
  pinMode(relay1Pin, OUTPUT);
  pinMode(relay2Pin, OUTPUT);
  Serial.begin(9600); // For debugging
  Serial.println("FSR System Initialized. Waiting for input...");
}

void loop() {
  int fsr1Value = analogRead(fsr1Pin)+100; // LEFT
  int fsr2Value = analogRead(fsr2Pin)+100; // RIGHT

  // Print values with clear labels
  Serial.print("LEFT (FSR1): ");
  Serial.print(fsr1Value);
  Serial.print(" | RIGHT (FSR2): ");
  Serial.println(fsr2Value);

  // LEFT Detection
  if (fsr1Value > threshold1) {
    digitalWrite(relay1Pin, LOW); // Turn ON Relay 1
    Serial.println("left");
  } else {
    digitalWrite(relay1Pin, HIGH); // Turn OFF Relay 1
    
  }

  // RIGHT Detection
  if (fsr2Value > threshold2) {
    digitalWrite(relay2Pin, LOW); // Turn ON Relay 2
    Serial.println("right");
  } else {
    digitalWrite(relay2Pin, HIGH); // Turn OFF Relay 2
    
  }

  Serial.println("-------------------------");
  delay(200); // Slightly longer delay for readability
}
