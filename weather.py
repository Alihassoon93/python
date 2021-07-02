import tkinter as tk
from tkinter.messagebox import showinfo
import requests
import json

# get the weather data 

def get_weather_data():
	API_KEY = "4453d639d0683bad314070a488951154"

	city = city_entry.get()
	URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

	res = requests.get(URL)
	json_data = json.loads(res.text)

	weather =  json_data["weather"][0]["description"]
	temperature = json_data["main"]["temp"]
	humidity = json_data["main"]["humidity"]
	wind_speed =  json_data["wind"]["speed"]

	showinfo(f'{city.title()} Weather',
		f'Weather: {weather} \n Temperature: {temperature} \n , Humidity: {humidity} \n Wind Speed: {wind_speed}')


# bulid the tkinter small ui 
win = tk.Tk()


win.title('Weather App')

app_label = tk.Label(win, text="Weather App", font=("Times", 20, "bold"))
app_label.grid(row=1, column=0, pady=10)

city_entry = tk.Entry(win, width=20)
city_entry.grid(row=1, column=1, pady=10)

btn = tk.Button(win, text="Get weather", bd=1, command=get_weather_data)
btn.grid(row=2, column=0, columnspan=2, pady=10)


# to keep the window open
win.mainloop()





