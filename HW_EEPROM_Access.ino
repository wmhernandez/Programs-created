#include <Arduino.h>
#include <EEPROM.h>

  int  bufcounter;
  char addrascii[3];
  int  addrcounter;

  int  xinterger;
  int  datacounter;
  char dataascii[3];
  
void setup() {
  Serial.begin(9600);
  Serial.println("Enter whether you wish to read from or write to EEPROM");
  Serial.println("the address followed by input data if writing.");

}

void readfunction(char readentry[13]) {  
  int address;                           // address will be an interger with the actual nubmeric value entered as a string.
  char addrascii[4];                    // addrascii will be the ascii representation of a numberic value for the address (0-254);
 
  bufcounter=5;
  addrcounter=0;

  while (readentry[bufcounter]!= 32 && readentry[bufcounter]!= 13 &&readentry[bufcounter]!= 0)       //32 is the ascii value for a blank space
  {
     addrascii[addrcounter]=readentry[bufcounter];
     addrcounter=addrcounter+1;
     bufcounter=bufcounter+1;
     }
   address=atoi(addrascii);             // address, entered as a string, is now an interger that can be used.
   Serial.print("address value is ");
   Serial.println(address);
   Serial.println();
   Serial.print("data value is ");
   Serial.println(EEPROM.read(address), DEC);
   readentry = 0;
 }

void writefunction(char writeentry[13]) {  
  int address;                           // address will be an interger with the actual nubmeric value entered as a string.

  bufcounter=6;
  addrcounter=0;
  datacounter=0;
  int data; 

  while (writeentry[bufcounter]!= 32)          //32 is the ascii value for a blank space
  {
     addrascii[addrcounter]=writeentry[bufcounter];
     addrcounter=addrcounter+1;
     bufcounter=bufcounter+1;
     address=atoi(addrascii);                 // address, entered as a string, is now an interger that can be used.
    }
   bufcounter=bufcounter+1;
   int finalbufchar = writeentry[bufcounter+2];

   while ((writeentry[bufcounter]!= 32)  && (writeentry[bufcounter]!= 13) && (writeentry[bufcounter]!= 0))      // 32 is the ascii value for a blank space, 13 for char return
  {
     dataascii[datacounter]=writeentry[bufcounter];
     datacounter=datacounter+1;
     bufcounter=bufcounter+1;
     data=atoi(dataascii);                // address, entered as a string, is now an interger that can be used.
     }
   finalbufchar = writeentry[bufcounter];
   EEPROM.write(address, 00);  
   EEPROM.write(address, data);
   Serial.print("The data in address ");
   Serial.print(address);
   Serial.print(" is ");
   Serial.println(EEPROM.read(address));

}

void loop() {
  if (Serial.available() > 0)  {
    char entry[] = "            ";    
    Serial.readBytes(entry, 13);
    Serial.println();
    Serial.print("you entered ");
    Serial.println(entry);
    Serial.println();
    if (entry[0]==114)    {             //ascii value for "r" is 114.  Use this to distinguish between "read" and "write"               
      readfunction(entry);  
    }      
    else if (entry[0]==119) {           //ascii value for "w" is 119.  Use this to distinguish between "read" and "write"  
        writefunction(entry);
      }
    else
    {
    Serial.println("You entered an incorrect request.");           
    }   
    memset(entry, 0,13);
    }
  }

