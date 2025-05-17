import pandas as pd
from datetime import datetime

def clean_data(raw_data_list):
    records = []

    for data in raw_data_list:
        if data:
            record = {
                "city": data["name"],
                "temperature_c": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "weather_main": data["weather"][0]["main"],
                "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            }
            records.append(record)

    df = pd.DataFrame(records)
    return df
