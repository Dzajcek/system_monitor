Monitor zasobów systemowych napisany w Pythonie, który śledzi zużycie procesora (CPU) oraz pamięci RAM, zapisuje dane do pliku CSV i generuje wykresy.

## 🚀 Funkcje
* **Monitoring w czasie rzeczywistym:** Logowanie zużycia CPU i RAM co 5 sekund.
* **Zapis do bazy danych:** Wszystkie dane trafiają do pliku `stats.csv`.
* **Automatyczne generowanie wykresu:** Po zakończeniu pracy (Ctrl+C) program automatycznie generuje wizualizację zebranych danych.
* **Odporność na błędy:** Skrypt sam zarządza ścieżkami plików i obsługuje przerwanie pracy przez użytkownika.

* ## 🛠️ Instalacja i uruchomienie

1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/TWOJA-NAZWA/system-monitor.git](https://github.com/TWOJA-NAZWA/system-monitor.git)

2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install psutil matplotlib
   
3. Uruchom program:
  ```bash
  python monitor.py

📝 Użycie
-Uruchom skrypt monitor.py.
-Aby zakończyć zbieranie danych i zobaczyć wykres, naciśnij Ctrl + C w terminalu.
-Wygenerowany wykres pokaże zmiany w czasie dla obu parametrów.

🏗️ Struktura plików
monitor.py - główny skrypt zarządzający pętlą i logowaniem.
show_plot.py - moduł odpowiedzialny za wczytywanie danych i rysowanie wykresów.
stats.csv - plik z danymi (generowany automatycznie).
