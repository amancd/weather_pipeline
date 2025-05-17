import sqlite3

def save_to_db(df, db_name="weather.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("weather_data", conn, if_exists="append", index=False)
    conn.close()
