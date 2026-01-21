import psutil
import datetime
from time import sleep
import csv

def info():
    cpu = psutil.cpu_percent(0.1)
    ram = psutil.virtual_memory().percent
    return [cpu, ram]

while True:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    data = info()
    cpu = data[0]
    ram = data[1]
    print(f"cpu {cpu}, ram {ram} = {time}")
    with open("stats.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time, cpu, ram])
    sleep(5)