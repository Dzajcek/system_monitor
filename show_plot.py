import matplotlib.pyplot as plt
import os
import sys
import csv



def _load_csv():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "stats.csv")
    if os.path.exists(file_path):
        times = []
        cpu_values = []
        ram_values = []
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                times.append(row[0])
                cpu_values.append(float(row[1]))
                ram_values.append(float(row[2]))
        
        return [times, cpu_values, ram_values]
    else:
        sys.exit("Plik stats.csv nie istnieje")

def draw_plot():

    # INFO
    data = _load_csv()
    times = data[0]
    cpu_values = data[1]
    ram_values = data[2]


    # WYKRES
    plt.figure(figsize=(10, 6))

    plt.plot(times, cpu_values, label="CPU %", color="red", linewidth=2)
    plt.plot(times, ram_values, label="RAM %", color="blue", linewidth=2)

    plt.title("Zuzycie zasobow systemowych", fontsize=16)
    plt.xlabel("Czas", fontsize=12)
    plt.ylabel("Uzycie (%)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.ylim(0, 100)

    plt.tight_layout()
    plt.show()