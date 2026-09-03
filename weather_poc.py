import urllib.request
import json
import os
from datetime import datetime

# Open-Meteo forecast API for ZIP 75024 (Plano, TX)
URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=33.0754&longitude=-96.8236"
    "&current=temperature_2m"
    "&temperature_unit=fahrenheit"
    "&timezone=America/Chicago"
)
OUTPUT_FILE = "temperature_log.txt"

def fetch_and_log_temperature():
    try:
        # 1. Ask the API for weather data
        req = urllib.request.Request(URL, headers={'User-Agent': 'CursorCloudAgentPOC/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        # 2. Grab the temperature reading
        current_data = data.get("current", {})
        temp = current_data.get("temperature_2m")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if temp is not None:
            log_line = f"{timestamp} | Temperature: {temp}°F\n"
            
            # 3. Write it into the file
            with open(OUTPUT_FILE, "a") as f:
                f.write(log_line)
                
            print(f"Success! Logged data: {log_line.strip()}")
        else:
            print("Error: Temperature data was missing in the API response.")
            
    except Exception as e:
        print(f"API failed to run: {e}")

if __name__ == "__main__":
    fetch_and_log_temperature()
