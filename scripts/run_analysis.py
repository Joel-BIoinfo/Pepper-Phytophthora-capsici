import requests
import pandas as pd
import matplotlib.pyplot as plt

print("1. Fetching monsoon weather data for Wayanad...")

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 11.685,
    "longitude": 76.132,
    "start_date": "2024-06-01",
    "end_date": "2024-08-31",
    "daily": ["temperature_2m_mean", "relative_humidity_2m_mean", "precipitation_sum"],
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)
data = response.json()["daily"]
df = pd.DataFrame(data)
df["time"] = pd.to_datetime(df["time"])

print("2. Calculating Phytophthora capsici infection risk...")

df["High_Risk"] = (
    (df["relative_humidity_2m_mean"] >= 85) &
    (df["temperature_2m_mean"] >= 22) & 
    (df["temperature_2m_mean"] <= 28) &
    (df["precipitation_sum"] >= 10)
)

df["Infection_Alert"] = df["High_Risk"] & df["High_Risk"].shift(1)

risk_days = df["Infection_Alert"].sum()
print(f"-> Detected {risk_days} critical infection alert days.")

print("3. Generating diagnostic chart...")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.bar(df["time"], df["precipitation_sum"], color="#3498db", label="Daily Rainfall (mm)")
ax1.set_ylabel("Rainfall (mm)")
ax1.set_title("Wayanad Monsoon Climate & Quick Wilt (P. capsici) Alert Windows")
ax1.legend(loc="upper left")
ax1.grid(True, linestyle="--", alpha=0.5)

ax2.plot(df["time"], df["relative_humidity_2m_mean"], color="#16a085", label="Relative Humidity (%)")
ax2.plot(df["time"], df["temperature_2m_mean"], color="#e67e22", label="Mean Temp (°C)")
ax2.set_ylabel("RH (%) / Temp (°C)")
ax2.set_xlabel("Date")

alert_points = df[df["Infection_Alert"]]
ax2.scatter(alert_points["time"], alert_points["relative_humidity_2m_mean"], 
            color="#e74c3c", s=60, zorder=5, label="Infection Alert (48-hr Window)")

ax2.legend(loc="lower left")
ax2.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("wayanad_disease_risk.png", dpi=300)
df.to_csv("monsoon_disease_data.csv", index=False)

print("4. Done! Saved 'wayanad_disease_risk.png' and 'monsoon_disease_data.csv' in your folder.")
