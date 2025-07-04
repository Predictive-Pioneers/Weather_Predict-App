import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "https://openweathermap.org/api"

def get_weather():
    city = city_entry.get()
    
    if city == "":
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        result = f"Temperature: {temp}°C\nDescription: {desc}\nHumidity: {humidity}%"
        weather_label.config(text=result)
    else:
        weather_label.config(text="City not found or invalid API key!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.resizable(False, False)
root.iconbitmap(r"cloudy.ico")

l = tk.Label(root, text="Enter City:", font=("Arial", 12))
l.pack(pady = 10)

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack()

btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="blue", fg="white")
btn.pack(pady = 10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
weather_label.pack(pady=10)

root.mainloop()
