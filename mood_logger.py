import tkinter as tk
from tkinter import messagebox
import datetime
import json
from pathlib import Path
import base64
from io import BytesIO
from PIL import Image, ImageTk
import sys


path = Path.home() / 'mood_logger'
path.mkdir(parents=True, exist_ok=True)

try:
    with open(path / 'mood_log.json', 'rb') as file:
        try:
            lines = file.readlines()
            lastline = lines[-1].decode('utf-8').strip()
            parsed = json.loads(lastline)
            date = parsed.get('date')
        except Exception as e:
            date = None
except FileNotFoundError:
    open(path / 'mood_log.json', 'w').close()
    date = None
if date == datetime.datetime.now().strftime('%Y-%m-%d'):
    sys.exit(1)

def log():
    try:
        messagebox.showinfo(title='Mood Logged', message='Your mood has been logged successfully!')
        mood = scale.get()
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        data = {
            'mood': mood,
            'date': date
        }
        with open(path / 'mood_log.json', 'a') as file:
            file.write(json.dumps(data) + '\n')
    except Exception as e:
        messagebox.showerror(title='Error', message='An error occurred while logging your mood.')
    window.destroy()

window = tk.Tk()
window.title('Mood Logger')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 

window_width = 300
window_height = 240

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJUExURQAAAP+7AAAAAACwewkAAAADdFJOU///ANfKDUEAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQ+SURBVHhe1ZhJkttIEAQ1+v+jx5ogkZGeW6HYoFF+EipjG2kOUv/5u8kfwPsqiXGKY7VC7Uyw9FG+LoeeniBvclxNC50N1NYhWjBDdwmVRYY8L6P+GsrSCPd4AR+dQ1ES4J4ugvSEIKHffW/AfBIEDHgbFoB4Z0DFfw5eFTY44pX2BN9tUHdypLLpQfJKt4elhHoHq/IBzQS25dBlsKgakC9gTwe9L1h0YQArJug/YNHyAMavwIwfWFQMoG1vQLaATfkAuh4wfQVmpGV8KPp3FjAhXRCf6HnB+An6D9gWB9AhsKKF5hehj98dLKmhU2AhPh0MYk2JtwE04lNJktiUQhNAo/9S0jSWJcARfyd9pftQijxfFoH8ZXEPrlN/rVSJWpYAtRnc28KAJlRPAEqn1sd8gCpcLHP9UYCu+e+4OADRPB44yZNSkA3QuzPSnN0peNBp4gC90hkLhvMDavIF2QD6Hsg9iHj7Qe8ncucAOeVe1lTvT9RoqKIeQNcLkYgMrwdwGqLxA+Sw5H4K+fKERkNV1QB6FJHV0OQQnQ7YsJfQA0S5MWBeQENAtOkA6gMSEKA2xeQ2oM/Au4iBmoLNvx8kA6gWfXgAgy05nQPsJcqzm7ydOFNuS27zADl1C5yHguYYBlBbJlXvS2c7HQMarZxwzt5OnClK5LQ/4HlzLyedrR1A5ZRUMdns9BUD1pT5vWCyyW0Y4KN4rBlscnQDqJuTKiabHacBGsVTx2Cz6zjAtDz09LbzujDgqebjTGezTv1fsFLfgLYaVN0Jux9QdIHLdnY/oKgG6usB7w0I+vAwc5YqFFVQfz3hvQHBEB4WMI9AUUEwhIcFzCNQVBAM4WEB8wgUFQRDeFjAPAJFBcEQHhYwj0BRQTCEhwXMI1BUQAe/lxCTQVEBHfxeQkwGRQW0CZTW0HlAVQFtJxTWqGv+CwlRt4PCGvOs/I0oYA4HZQ1m+jcH5Aso6jDX9A+THLEYFDWIa29ANoGKDrEN/zitkYyrVvcnsD3AT+BtwIzTDyjuQQq/Y8Dun8E22j/9mO4OpO5bBnz4z8D1c8AHFkjZ1o/r32YYcPsC9H/LgM8tYH8y4NYF2uMGfOq3IPRnA25coC0Y8JnfgtifDrhtgXaEAR9YoA1We/7q9gWaL61fNODmBZqupcWAX1/gwosBdy5w0a5TP+5b4IJ9pfu6a4GLRSM+HczZxaei0X/essBnshDfWPALExAY+vjw2wsQx7ZkwO8uQBi70gFc8MYEJrGpGBAWbE5gSt7Fhwd0bi1gRlHFhwN6r0+gv+ivBiQLLk2gt+wvB6QTFjfQ9QPTT+pLumDeQP0Bs43mVCxoRlB3wmShuzUTwgpeFaY6+ms/YQ0mgun+9gLmkVHw3gRmRRYk+xOYk7Ek2pvAjJxF2fUNtFcsCy9NoLPhinZxAz09F+U/sFChdmbDcvB+9cH/Oj83tbCA5yUAAAAASUVORK5CYII="

icon_data = base64.b64decode(icon_base64)
image = Image.open(BytesIO(icon_data))
photo = ImageTk.PhotoImage(image)

window.iconphoto(False, photo)

window.configure(bg='white')

label = tk.Label(window, text="What's your mood?", font=('Arial', 20), bg='white', fg='black')
label.pack(pady=20)

scale = tk.Scale(window, from_=1, to=10, orient='horizontal', length=200, bg='white', fg='black')
scale.set(5)
scale.pack(pady=10)

button = tk.Button(window, text='confirm', command=log, bg='white', fg='black', font=('Arial', 14))
button.pack(pady=20)

window.mainloop()