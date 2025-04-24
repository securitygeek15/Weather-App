import customtkinter as ctk
import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    b_url = "http://api.weatherapi.com/v1/current.json"

    try:
        response = requests.get(b_url, params={'key': api_key, 'q': city})
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", f"Error: {data['error']['message']}")
        else:
            location = data['location']['name']
            country = data['location']['country']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']

            result_label.configure(text=f"{location}, {country}\nTemperature: {temperature}°C\nCondition: {condition}")
            result_label.configure(text_color="#2D9CDB")

    except Exception as E:
        messagebox.showerror("Error", f"An error occurred: {E}")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather App")
root.geometry("500x400")

header_label = ctk.CTkLabel(root, text="Weather App", font=("Arial", 24, "bold"), text_color="#FF5733")
header_label.pack(pady=20)

city_label = ctk.CTkLabel(root, text="Enter City:", font=("Arial", 14))
city_label.pack(pady=10)

city_entry = ctk.CTkEntry(root, width=250, height=40, font=("Arial", 14), border_width=2, placeholder_text="City Name")
city_entry.pack(pady=5)

get_weather_button = ctk.CTkButton(root, text="Get Weather", font=("Arial", 16), command=get_weather)
get_weather_button.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 16), text_color="#FFFFFF", wraplength=400)
result_label.pack(pady=20)

root.mainloop()
