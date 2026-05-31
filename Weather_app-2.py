"""
Weather App with City Dropdown
------------------------------
A Tkinter GUI weather application where the user picks a city
from a dropdown (Combobox) and the current weather is fetched
from the free Open-Meteo API (NO API KEY REQUIRED).

Shows:
  - Condition
  - Temperature (degrees Celsius)
  - Humidity (percent)
  - Wind Speed (km/h)
  - Wind Direction (compass + degrees)

Run:
    python weather_app.py
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime


# ----- City list with latitude / longitude -----
CITIES = {
    "Asansol, West Bengal, India":        (19.0760,  72.8777),
    "Dhanbad, Jharkhand, India":         (28.6139,  77.2090),
    "Ranchi, Jharkhand, India":         (12.9716,  77.5946),
    "Nagpur, Maharastra, India":         (22.5726,  88.3639),
    "Bilaspur, Chhattisgarh, India":  (13.0827,  80.2707),
    "Singrauli, Madhya Pradesh, India":     (17.3850,  78.4867),
    "Bhubaneswar, Odisha, India":   (18.5204,  73.8567),
    "Kolkata, West Bengal, India":        (26.9124,  75.7873),
    "Varanasi, Uttar Pradesh, India":      (25.3176,  82.9739),
    "Raipur, Chhattisgarh, India":       (35.6762, 139.6503),
    "Delhi, India":         (46.8688, 151.2093),
    "Tokyo, Japan":         (48.8566,   2.3522),
    "Sydney, Australia":   (25.2048,  55.2708),
                           
    "Dubai, UAE":           (43.6532, -79.3832),
    "Singapore":             (1.3521, 103.8198),
    "Toronto, Canada":      (-33.9249,  18.4241),
    "Moscow, Russia":       (43.6532, -79.3832),
                             
                           
}


WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    77: "Snow grains",
    80: "Rain showers", 81: "Heavy rain showers", 82: "Violent showers",
    85: "Snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Severe thunderstorm",
}


def degrees_to_compass(deg: float) -> str:
    points = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
              "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return points[int((deg / 22.5) + 0.5) % 16]


def fetch_current_weather(lat: float, lon: float) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,"
        "wind_speed_10m,wind_direction_10m,weather_code"
        "&timezone=auto"
    )
    with urlopen(url, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))["current"]


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("440x540")
        self.configure(bg="#1e3a5f")
        self.resizable(False, False)

        tk.Label(self, text="Weather App",
                 font=("Segoe UI", 22, "bold"),
                 bg="#1e3a5f", fg="#ffd166").pack(pady=(20, 5))

        tk.Label(self, text="Select a city from the dropdown",
                 font=("Segoe UI", 10, "italic"),
                 bg="#1e3a5f", fg="#a9c5e8").pack(pady=(0, 10))

        # ---- Dropdown row ----
        frm = tk.Frame(self, bg="#1e3a5f")
        frm.pack(pady=10)

        tk.Label(frm, text="City:", font=("Segoe UI", 11),
                 bg="#1e3a5f", fg="white").grid(row=0, column=0, padx=(0, 8))

        self.city_var = tk.StringVar()
        self.city_combo = ttk.Combobox(
            frm, textvariable=self.city_var,
            values=list(CITIES.keys()),
            state="readonly",
            width=24, font=("Segoe UI", 11),
        )
        self.city_combo.grid(row=0, column=1, padx=(0, 8))
        self.city_combo.current(0)
        self.city_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        ttk.Button(frm, text="Get Weather", command=self.refresh)\
            .grid(row=0, column=2)

        # ---- Result card ----
        self.card = tk.Frame(self, bg="#274c77")
        self.card.pack(pady=20, padx=20, fill="x")

        self.lbl_city = tk.Label(self.card, text="-",
                                 font=("Segoe UI", 16, "bold"),
                                 bg="#274c77", fg="white")
        self.lbl_city.pack(pady=(15, 5))

        self.lbl_cond = tk.Label(self.card, text="",
                                 font=("Segoe UI", 12, "italic"),
                                 bg="#274c77", fg="#cfe0ff")
        self.lbl_cond.pack(pady=(0, 10))

        self.lbl_temp = tk.Label(self.card, text="--°C",
                                 font=("Segoe UI", 40, "bold"),
                                 bg="#274c77", fg="#ffd166")
        self.lbl_temp.pack(pady=(0, 15))

        self.lbl_humidity   = self._make_row("Humidity",       "-- %")
        self.lbl_wind_speed = self._make_row("Wind Speed",     "-- km/h")
        self.lbl_wind_dir   = self._make_row("Wind Direction", "--")

        tk.Frame(self.card, bg="#274c77", height=15).pack()

        self.lbl_updated = tk.Label(self, text="",
                                    font=("Segoe UI", 9),
                                    bg="#1e3a5f", fg="#a9c5e8")
        self.lbl_updated.pack(side="bottom", pady=10)

        self.after(200, self.refresh)

    def _make_row(self, label_text: str, default: str) -> tk.Label:
        row = tk.Frame(self.card, bg="#274c77")
        row.pack(fill="x", padx=25, pady=4)
        tk.Label(row, text=label_text, font=("Segoe UI", 11),
                 bg="#274c77", fg="#cfe0ff", anchor="w").pack(side="left")
        val = tk.Label(row, text=default, font=("Segoe UI", 11, "bold"),
                       bg="#274c77", fg="white", anchor="e")
        val.pack(side="right")
        return val

    def refresh(self):
        city = self.city_var.get()
        if city not in CITIES:
            messagebox.showwarning("Select a city",
                                   "Please choose a city from the dropdown.")
            return

        lat, lon = CITIES[city]
        try:
            cur = fetch_current_weather(lat, lon)
        except (URLError, HTTPError) as e:
            messagebox.showerror("Network error",
                                 f"Could not reach Open-Meteo:\n{e}")
            return
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        temp  = cur["temperature_2m"]
        hum   = cur["relative_humidity_2m"]
        wspd  = cur["wind_speed_10m"]
        wdir  = cur["wind_direction_10m"]
        wcode = cur["weather_code"]

        self.lbl_city.config(text=city)
        self.lbl_cond.config(text=WEATHER_CODES.get(wcode, "Unknown"))
        self.lbl_temp.config(text=f"{temp:.1f}°C")
        self.lbl_humidity.config(text=f"{hum} %")
        self.lbl_wind_speed.config(text=f"{wspd:.1f} km/h")
        self.lbl_wind_dir.config(text=f"{degrees_to_compass(wdir)}  ({wdir:.0f}°)")
        self.lbl_updated.config(
            text=f"Last updated: {datetime.now().strftime('%d %b %Y, %H:%M:%S')}"
        )


if __name__ == "__main__":
    WeatherApp().mainloop()
