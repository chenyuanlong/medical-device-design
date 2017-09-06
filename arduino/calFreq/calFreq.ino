#define SENSORPIN A0

void setup() {
  Serial.begin(9600);
  delay(100);
}

double alpha=0.75;
int period=50;
double change=0.0;
double max1=0.0;

unsigned long time1=0;
unsigned long time2;
int count=0;

void loop() {
  static double oldValue=1009;
  static double oldChange=0.2;

  int rawValue=analogRead(SENSORPIN);
  double value= alpha*oldValue +(1-alpha)* rawValue;
  change=value-oldValue;
  
  if (change >= max1) {
    max1= change;
    Serial.println(" |");
  } else {
    Serial.println("|");
  }

  max1 = max1 * 0.98;

  oldValue=value;
  oldChange=change;
  delay(period);
}
