// demo: CAN-BUS Shield, receive data with check mode
// send data coming to fast, such as less than 10ms, you can use this way
// loovee, 2014-6-13

#include <SPI.h>

#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "HIGHT_core.h"
#include "HIGHT_core.c"

#define CAN_2515
// #define CAN_2518FD

// Set SPI CS Pin according to your hardware

#if defined(SEEED_WIO_TERMINAL) && defined(CAN_2518FD)
// For Wio Terminal w/ MCP2518FD RPi Hat：
// Channel 0 SPI_CS Pin: BCM 8
// Channel 1 SPI_CS Pin: BCM 7
// Interupt Pin: BCM25
const int SPI_CS_PIN  = BCM8;
const int CAN_INT_PIN = BCM25;
#else

// For Arduino MCP2515 Hat:
// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 10;
const int CAN_INT_PIN = 2;
#endif


#ifdef CAN_2518FD
#include "mcp2518fd_can.h"
mcp2518fd CAN(SPI_CS_PIN); // Set CS pin
#endif

#ifdef CAN_2515
#include "mcp2515_can.h"
mcp2515_can CAN(SPI_CS_PIN); // Set CS pin
#endif

const int LED        = 8;
boolean ledON        = 1;
unsigned char perstep[8] = {00, 00, 00, 00, 00, 00, 00, 00};
void setup() {
    SERIAL_PORT_MONITOR.begin(115200);
    pinMode(LED, OUTPUT);

    while (CAN_OK != CAN.begin(CAN_500KBPS)) {             // init can bus : baudrate = 500k
        SERIAL_PORT_MONITOR.println("CAN init fail, retry...");
        delay(100);
    }
    SERIAL_PORT_MONITOR.println("CAN init ok!");
    CAN.sendMsgBuf(0x44, 0, 8, perstep);
    SERIAL_PORT_MONITOR.println("Send one");
    pinMode(8, OUTPUT);
    digitalWrite(8, HIGH);
    delay(1000);
    digitalWrite(8, LOW);
    delay(1000);
 
}
int Cnt;

BYTE key1 [16]={0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01}; 
BYTE key2 [16]={0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12};
BYTE key3 [16]={0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23}; 
BYTE key4 [16]={0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34}; 
BYTE key5 [16]={0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45};
 
BYTE KEY [5]= {key1, key2, key3, key4, key5};
BYTE pdwpdwRoundKey[136] = {0,};
BYTE pbData[8] = {0};

int keynum = 0;
int cnt = 0;

void loop() {
    unsigned char len = 0;
    unsigned char buf[8];

    if (CAN_MSGAVAIL == CAN.checkReceive()) {// check if data coming
      
        CAN.readMsgBuf(&len, buf); // read data,  len: data length, buf: data buf

        int (receive_id)=CAN.getCanId();
        int result =442;
        for(int i=1; i<23; i++)
        {
          if(result > 441){          
          result=receive_id -i;
          }
        }
        
        for(int i = 0; i < 8; i++)
        {
           pbData[i] = buf[i];
          }

        if (cnt == 20){
        	cnt = 0;
              	keynum = keynum +1;
              	}

      	if (keynum == 5){
              	keynum = 0;
       	}

        HIGHT_Key( KEY[keynum], pdwpdwRoundKey );  

        cnt = cnt+1;
        
        if(result == 0x1b9) {
          Cnt=++Cnt;
          SERIAL_PORT_MONITOR.println(Cnt);
          unsigned long canId = CAN.getCanId();
          digitalWrite(8, HIGH);
        
        SERIAL_PORT_MONITOR.println("\n-----------------------------");
        SERIAL_PORT_MONITOR.print("ID: 00000");
        SERIAL_PORT_MONITOR.print(result, HEX);
        SERIAL_PORT_MONITOR.print("  DLC 8      ");
        for (int i = 0; i < 8; i++) { // print the data
            SERIAL_PORT_MONITOR.print(pbData[i],HEX);
            SERIAL_PORT_MONITOR.print("\t");
        HIGHT_Dec( pdwpdwRoundKey, pbData );
        for(int i=0;i<8;i++){
          Serial.print(pbData[i],HEX);
          Serial.println("");
          delay(1000); 
        }    
        }
        }
        SERIAL_PORT_MONITOR.println("Receive Data");
        SERIAL_PORT_MONITOR.println();
        

       
    
}
}


//END FILE
