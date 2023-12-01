import tkinter as tk
import requests
import time
from datetime import datetime, timedelta

def get_weather():
    city = text_field.get()
    api_key = '33463c2ba5de43f8c3ff2f4836f7c4f0'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    try:
        json_data = requests.get(api_url).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)

        # Use datetime for correct time formatting
        sunrise_utc = datetime.utcfromtimestamp(json_data['sys']['sunrise'])
        sunset_utc = datetime.utcfromtimestamp(json_data['sys']['sunset'])

        # Convert to local time
        sunrise_local = sunrise_utc + timedelta(seconds=json_data['timezone'])
        sunset_local = sunset_utc + timedelta(seconds=json_data['timezone'])

        # Format time as string without seconds and with AM/PM
        sunrise = sunrise_local.strftime('%I:%M %p')
        sunset = sunset_local.strftime('%I:%M %p')

        final_info = f'{condition}\n{temp}°C'
        final_data = f'\nMax Temp: {max_temp}\nMin Temp: {min_temp}\nSunrise: {sunrise}\nSunset: {sunset}'
        label1.config(text=final_info)
        label2.config(text=final_data)
    except requests.exceptions.RequestException as e:
        label1.config(text='Error fetching data')
        label2.config(text=str(e))

canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather App')

font_large = ('poppins', 35, 'bold')
font_small = ('poppins', 15, 'bold')

text_field = tk.Entry(canvas, font=font_large)
text_field.pack(pady=20)
text_field.focus()
text_field.bind('<Return>', lambda event: get_weather())

label1 = tk.Label(canvas, font=font_large)
label1.pack()
label2 = tk.Label(canvas, font=font_small)
label2.pack()

canvas.mainloop()
















