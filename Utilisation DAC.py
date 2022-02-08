import Adafruit_MCP4725
import time

dac = Adafruit_MCP4725.MCP4725(address=0x60)

while True:
    for x in range(0,4097,int(4097/(12*5))):
        
        print(x)
        dac.set_voltage(x)
        voltage = x/4096.0*5.0
        time.sleep(0.5) 
