import tkinter as tk
import requests
import time


def get_weather(canvas):
    city = text_field.get()
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city + '&appid=35adcd283bb71e7e38c3dc2618e914ed'
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunset'] - 21600))

    final_info = condition + '\n' + str(temp) + '°C'
    final_data = '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min Temp: ' + str(
        min_temp) + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Sunrise: ' + sunrise + '\n' + 'Sunset: ' + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather App')

f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

text_field = tk.Entry(canvas, font=t)
text_field.pack(pady=20)
text_field.focus()
text_field.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
