import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# window setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#d0e7f9")
root.resizable(False, False)
root.iconbitmap(r"/cloudy.ico")


l = tk.Label(root, text="Enter City Name", font=("Arial", 14, "bold"), bg="#d0e7f9")
l.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 13), justify="center", width=25)
city_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left", bg="#d0e7f9")
result_label.pack(pady=10)


def get_weather():
    city_name = city_entry.get().strip()
    API_key = 'e969431725b98b7dff5e668397794371'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    if city_name == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        current_time = datetime.now().strftime('%d-%b-%Y %I:%M %p')

        result = (
            f"🌁 City: {city_name}\n"
            f"🕒 Time: {current_time}\n\n"
            f"🌤 Description: {description}\n"
            f"🌡 Temperature: {temp}°C\n"
            f"🤗 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%"
        )
        result_label.config(text=result)
    else:
        result_label.config(text="City not found or invalid API key.")

def clear_all():
    city_entry.delete(0, tk.END)
    result_label.config(text="")

# Buttons
btn1 = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#007acc", fg="white", width=15)
btn1.pack(pady=10)
btn2 = tk.Button(root, text="Clear", command=clear_all, font=("Arial", 10), bg="#f0ad4e", fg="white", width=10)
btn2.pack(pady=5)

footer = tk.Label(root, text="© Made by Arpita 💙", font=("Arial", 9), bg="#d0e7f9", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
