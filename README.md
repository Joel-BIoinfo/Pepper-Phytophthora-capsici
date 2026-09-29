# Pepper-Phytophthora-capsici
Tracking monsoon weather and Quick Wilt disease risks for Piper nigrum in Wayanad, Kerala.
 Project Overview
This repository contains epidemiological and meteorological analysis evaluating infection risk windows for Quick Wilt (Phytophthora capsici) affecting crops in Wayanad, India during the monsoon season (June–August 2024).

- Methodology & Risk Thresholds
We track Open-Meteo weather data [cite: 1] to flag 48-hour critical risk windows for plant infections based on local environmental factors
The parameters:

* Relative Humidity : 85% or higher
* Mean Temperature: Between 22°C and 28°C
* Daily Precipitation: 10 mm or higher
* Sustained Duration: When these bad weather conditions stick around for multiple days in a row, building up real infection pressure.

Repository Contents
## Repository Contents
* `scripts/run_analysis.py`: Python automation script utilizing pandas, requests, and matplotlib.
* `data/monsoon_disease_data.csv`: Daily processed time-series dataset featuring computed risk columns.
* `outputs/wayanad_disease_risk.png`: Dual-panel diagnostic chart depicting daily rainfall bars alongside relative humidity, mean temperature trends, and highlighted alert windows.
