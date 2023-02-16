 #include <Wire.h>  
 #include <LiquidCrystal_I2C.h>  
 LiquidCrystal_I2C lcd(0x27,16,2);  
 int val = 0 ;  
 void setup()  
 {  
 Serial.begin(9600);  
 lcd.init();  
 lcd.backlight
 ();  
 pinMode(3,INPUT); // pir sensor output pin connected  
 pinMode(4,OUTPUT);  
 pinMode(5,OUTPUT);  
 pinMode(6,OUTPUT);  
 digitalWrite(4,HIGH);  
 lcd.setCursor(0,0);  
 lcd.print("Mayo College");  
 }  
 void loop()  
 {  
 val = digitalRead(3); // soil moisture sensor output pin connected  
 Serial.println(val); // see the value in serial monitor in Arduino IDE  
 delay(1000);  
 if(val == 1 )  
 {  
 digitalWrite(4,HIGH);  
 digitalWrite(5,HIGH);  
 digitalWrite(6,LOW);  
 lcd.setCursor(0,1);  
 lcd.print(" PUMP ON ");  
 }  
 else  
 {  
 digitalWrite(4,LOW);  
 digitalWrite(5,LOW);  
 digitalWrite(6,HIGH);  
 lcd.setCursor(0,1);  
 lcd.print(" PUMP OFF ");  
 }  
 }  
