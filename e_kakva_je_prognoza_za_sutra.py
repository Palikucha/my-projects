import tkinter as tk
import requests
import sqlite3
from datetime import datetime

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.url, params=params)
        data = response.json()
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")
        if 'name' not in data:
            raise Exception(f"No weather data found for city {city}")
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity']
        }

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                city TEXT,
                temperature REAL,
                pressure INTEGER,
                humidity INTEGER
            )
        """)
        self.conn.commit()

        # Add the new column
        self.cursor.execute("""
            PRAGMA table_info(weather)
        """)
        if 'time' not in [column[1] for column in self.cursor.fetchall()]:
            self.cursor.execute("""
                ALTER TABLE weather
                ADD COLUMN time TEXT
            """)
            self.conn.commit()

        #  da mi ne baca error
        self.cursor.execute("PRAGMA table_info(weather)")
        if 'fetched_at' not in [column[1] for column in self.cursor.fetchall()]:
            # If it doesn't, add it SUKA BLYAT
            self.cursor.execute("ALTER TABLE weather ADD COLUMN fetched_at TIMESTAMP")

   

   # bonus zadatak (PREZIREM SQL IZ DNA DUŠE)

    def get_last_fetched(self, city):
        self.cursor.execute("""
            SELECT fetched_at FROM weather
            WHERE city = ?
            ORDER BY fetched_at DESC
            LIMIT 1
        """, (city,))
        result = self.cursor.fetchone()
        return result[0] if result else None

   

    def insert_data(self, data):
        data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO weather (city, temperature, pressure, humidity, time)
            VALUES (:city, :temperature, :pressure, :humidity, :time)
        """, data)
        self.conn.commit()

class App(tk.Tk):
    def __init__(self, client, db):
        super().__init__()
        self.client = client
        self.db = db
        self.title("Vakula je rekao:")
        self.geometry("400x200")
        self.configure(bg="#ccd9ff")
        self.create_widgets()

    def create_widgets(self):
        self.entry_frame = tk.Frame(self, padx=10, pady=10, bg="#ccd9ff") #znam da sam mogao self.bg_image=tk.photoimage(file="slika.jpg") i onda self.configure(image=self.bg_image) ali mi se nije dalo komplicirati kod koji funkcionira :p
        self.entry_frame.grid(row=0, column=0, sticky='ew')

        self.entry_label = tk.Label(self.entry_frame, text="City:", font=("Helvetica", 14), bg="#ccd9ff")
        self.entry_label.pack(side='left')

        self.entry = tk.Entry(self.entry_frame)
        self.entry.pack(side='left', fill='x', expand=True)
        self.entry.bind("<Return>", lambda event: self.load_weather()) 

        self.load_button = tk.Button(self.entry_frame, text="Load", command=self.load_weather, font=("Helvetica", 14), bg="#ffb380") #malo kurčenja sa hex bojama
        self.load_button.pack(side='left')

        self.result_frame = tk.Frame(self, padx=10, pady=10, bg="#ccd9ff")
        self.result_frame.grid(row=1, column=0, sticky='nsew')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.result_labels = {
            'city': (tk.Label(self.result_frame, text="City:", font=("Helvetica", 14), bg="#ccd9ff"), tk.Label(self.result_frame, font=("Helvetica", 14), bg="#ccd9ff")),
            'temperature': (tk.Label(self.result_frame, text="Temperature (°C):", font=("Helvetica", 14), bg="#ccd9ff"), tk.Label(self.result_frame, font=("Helvetica", 14), bg="#ccd9ff")),
            'pressure': (tk.Label(self.result_frame, text="Pressure (hPa):", font=("Helvetica", 14), bg="#ccd9ff"), tk.Label(self.result_frame, font=("Helvetica", 14), bg="#ccd9ff")),
            'humidity': (tk.Label(self.result_frame, text="Humidity (%):", font=("Helvetica", 14), bg="#ccd9ff"), tk.Label(self.result_frame, font=("Helvetica", 14), bg="#ccd9ff"))  #ctrl + H : FTW BRUH
        }
        
        for i, (key, labels) in enumerate(self.result_labels.items()):
            name_label, value_label = labels
            name_label.grid(row=i, column=0, sticky='e', padx=(40, 0))  # padding za lijevu stranu NEMOJ ZABORAVIT OVO
            value_label.grid(row=i, column=1, sticky='w')

        self.status_bar = tk.Label(self, text="Enter a city and click Load", bd=1, relief='sunken', anchor='w')
        self.status_bar.grid(row=2, column=0, sticky='ew')

    def load_weather(self):
        city = self.entry.get()
        try:
            # bonus zadatak (zašto sam si ovo išao raditi?)
            last_fetched = self.db.get_last_fetched(city)
            if last_fetched and (datetime.now() - last_fetched).total_seconds() < 60:
                
                weather = self.db.get_data(city)
            else:
                
                weather = self.client.get_weather(city)
                
                self.db.insert_data(weather)

            for key, (name_label, value_label) in self.result_labels.items():
                value_label.config(text=weather[key])
            self.status_bar.config(text="Weather loaded successfully")
        except Exception as e:
            self.status_bar.config(text=str(e))
if __name__ == "__main__":
    api_key = "3a42368310ca0dc645075fd7fb51c3b8"
    client = Client(api_key)
    db = Database("weather.db")
    app = App(client, db)
    app.mainloop()