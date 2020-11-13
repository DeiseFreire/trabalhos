# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# controlando arduino pelo celular
# https://www.youtube.com/watch?v=hTkELLTYNnw
# -------------------------------------------------------------------------------------------

int led = 9;
char c;
void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}
void loop(){
 c=Serial.read();
     if(c == '1'){
 digitalWrite(led, HIGH);
}
     if(c == 'A'){
 digitalWrite(led, LOW);
    }
  }
  digitalWrite(led, estado);
}
