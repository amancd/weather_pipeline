from extract import fetch_weather_data
from transform import clean_data
from load import save_to_db
from config import CITIES

def run_pipeline():
    raw_data = [fetch_weather_data(city) for city in CITIES]
    cleaned_data = clean_data(raw_data)
    print("Cleaned Data:\n", cleaned_data)
    save_to_db(cleaned_data)
    print("Data saved to weather.db")

if __name__ == "__main__":
    run_pipeline()