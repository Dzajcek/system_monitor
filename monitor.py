import psutil
import datetime
from time import sleep
import csv
from show_plot import draw_plot
import os

def info():
    cpu = psutil.cpu_percent(0.1)
    ram = psutil.virtual_memory().percent
    return [cpu, ram]


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "stats.csv")
    print("Monitorowanie. Wcisnij ctrl+c, aby zakonczyc i wyswietlic wykres.")
    while True:
        try:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            data = info()
            cpu = data[0]
            ram = data[1]
            print(f"cpu {cpu}, ram {ram} = {time}")
            with open(file_path, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([time, cpu, ram])


            sleep(5)
        except KeyboardInterrupt:
            print("\nGenerowanie wykresu...")
            print("Program zostal wstrzymany zamknij wykres aby kontynuowac dzialanie.")
            draw_plot()
            
    
    