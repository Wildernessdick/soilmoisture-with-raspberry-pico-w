# Import necessary modules
import machine
import network
import secrets
import ssd1306
import utime

# Set up network connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
while not wlan.isconnected():
    utime.sleep(1)
deviceIp = wlan.ifconfig()[0]
print("Connected to Wi-Fi. IP address:", deviceIp)

# Set up soil moisture sensor
soil = machine.ADC(machine.Pin(26))
moistureMin = 18700 # When wet
moistureMax = 44074 # When dry
print("ADC:", soil.read_u16())

# Set up OLED display
displayWidth = 128
displayHeight = 64
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=200000)
oled = ssd1306.SSD1306_I2C(displayWidth, displayHeight, i2c)

# Main loop
while True:
    oled.fill(0)
    moisture = (moistureMax - soil.read_u16()) * 100 / (moistureMax - moistureMin)

    # Display moisture level
    oled.text("{:.0f}%".format(moisture), 92, 8)

    # Display device IP address
    oled.text(deviceIp, 12, 42)

    # Display ADC value
    oled.text("ADC: {}".format(soil.read_u16()), 12, 52)

    # Display moisture level as bar graph
    oled.rect(12, 18, 104, 20, 1) # Frame
    oled.fill_rect(14, 20, int(moisture), 16, 1) # Filling

    oled.show()

    # Print moisture level to console
    if moisture > 40:
        print("Moisture level: {}%".format(int(moisture)))
    else:
        print("Dry. Moisture level: {}%".format(int(moisture)))

    # Wait for specified interval before updating display and moisture level
    utime.sleep(10)
