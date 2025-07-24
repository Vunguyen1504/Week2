import serial
import time
from datetime import datetime

# 1. Connect to Arduino serial port
ser = serial.Serial('/dev/cu.usbmodem101', 9600)  # Update the port as needed
time.sleep(2)

# 2. Create output CSV file
filename = "dht22_data.csv"

# 3. Start logging loop
try:
    with open(filename, 'a') as file:
        while True:
            line = ser.readline().decode().strip()
            if "," in line:
                timestamp = datetime.now().strftime('%Y: %m: %d: %H: %M: %S:')
                file.write(f"{timestamp},{line}\n")
                print(f"{timestamp},{line}")
            time.sleep(3)  # wait 3 seconds
except KeyboardInterrupt:
    print("Stopped.")
