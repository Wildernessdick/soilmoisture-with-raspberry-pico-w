# Pico with Soil Moisture Reader and Display

This project uses a Pico microcontroller to read soil moisture levels and display them on an OLED display. 

## Getting Started
<img src="https://raw.githubusercontent.com/Wildernessdick/soilmoisture-with-raspberry-pico-w/main/setupOn.jpg?token=GHSAT0AAAAAABZQAD5VT5YGG5PI3N7T5IAKZAKBX7Q" alt="Setup On" width="666"/>


### Prerequisites

Before getting started with this project, make sure you have the following components and software:

- Raspberry Pi Pico microcontroller
- Soil moisture sensor
- OLED display
- Micro-USB cable
- Computer with Thonny or another MicroPython editor installed
- MicroPython firmware installed on the Pico

### Installing

1. Connect the soil moisture sensor to the Pico using jumper wires. Make sure to connect the power, ground, and signal pins correctly.
2. Connect the OLED display to the Pico using jumper wires. Make sure to connect the power, ground, and data pins correctly.
3. Open your MicroPython editor and create a new file for the code.
4. Import the necessary libraries and functions for the project, including `machine`, `time`, `ssd1306`, and `ADC`.
5. Define the pin numbers for the soil moisture sensor and the OLED display.
6. Initialize the OLED display and create a function to display the soil moisture levels on the screen.
7. Create a loop to read the soil moisture levels using the ADC function, and call the display function to show the levels on the OLED display.

### Usage

To use the project, follow these steps:

1. Configure the WLAN settings in the `secrets.py` file with your own network credentials.
2. Upload the code to the Pico using your MicroPython editor.
3. Connect the Pico to your computer using the micro-USB cable.
4. Open a serial terminal and connect to the Pico to view the output.
5. Place the soil moisture sensor in the soil and observe the levels displayed on the OLED screen.



## Acknowledgments

- Thanks to [stlehmann](https://github.com/stlehmann) for the `ssd1306.py` file.
- Part of the code is from unknown coder.
