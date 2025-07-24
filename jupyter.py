import matplotlib.pyplot as plt
import csv

timestamps, temps, hums = [], [], []

with open("dht22_data.csv") as file:
    for row in csv.reader(file):
        if len(row) == 3:
            ts, temp, hum = row
            try:
                temps.append(float(temp))
                hums.append(float(hum))
                timestamps.append(ts[-6:])  # only time part HHMMSS
            except:
                continue

plt.figure(figsize=(10, 5))
plt.plot(timestamps, temps, label="Temperature (°C)", color='red')
plt.plot(timestamps, hums, label="Humidity (%)", color='blue')
plt.xlabel("Time (HHMMSS)")
plt.ylabel("Values")
plt.title("Temperature & Humidity Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
