import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather
from utils import format_weather

def run_gui():
    window =tk.Tk()
    window.title("Weather Dashboard")
    window.geometry("400x250")

    city_entry =tk.Entry(window,width=30, font=("Arial",14))
    city_entry.pack(pady=20)

    output_label =tk.Label(window,text="",font=("Arial", 12),justify="left")
    output_label.pack(pady=10)

    def search_weather():
        city=  city_entry.get()
        if not city:
            messagebox.showwarning("Input Error","Please enter a city name!")
            return
        
        data =get_weather(city)
        output_label.config(text=format_weather(data))

    search_btn =tk.Button(window,text="Get Weather",command=search_weather)
    
    search_btn.pack()
    window.mainloop()