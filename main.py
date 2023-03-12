from machine import ADC, Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import socket
import network
import secrets
# Network settings
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

if wlan.isconnected() == False:
    deviceIp ="No ip"    
    utime.sleep(1)
        
ipconfig = wlan.ifconfig()
deviceIp = ipconfig[0]
print("Connected to wifi" )    

# Moisture sensor settings
soil = ADC(Pin(26)) # Soil moisture PIN reference 
# Calibration of capacitive soil sensor
min=18700 #When wet
max=44074 #When dry
print("ADC: "+str(soil.read_u16()))

# How often the information is updated
# 1 sec = 1
interval = 10

# Display settings
width  = 128                                         
height = 64                                    
fill = 1
nofill = 0
theme = False #False or True, as u like
              
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(width, height, i2c)    
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
print("")

while True:

    oled.fill(0)
    oled.invert(theme)
    moisture = (max-soil.read_u16())*100/(max-min)
           
    # OLEDTXT   
    oled.text("%.0f" % moisture +"%",92,8)
    oled.text(deviceIp,12,42 )
    oled.text("ADC:"+str(soil.read_u16()) ,12,52)
    
    # OLEDBAR
    oled.rect(12, 18, 104, 20, fill) #frame
    oled.fill_rect(14, 20, int(moisture), 16, fill)  #filling
    
    oled.show()
    
    if moisture > 40:
        print("moist", int(moisture),"%")
    else:
        print("dry", int(moisture),"%")
    
    utime.sleep(interval) 
    
    
    




