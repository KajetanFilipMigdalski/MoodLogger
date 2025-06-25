import tkinter as tk
import json
from pathlib import Path
import base64
from io import BytesIO
from PIL import Image, ImageTk

path = Path.home() / 'mood_logger'
path.mkdir(parents=True, exist_ok=True)

window = tk.Tk()
window.title('Mood Summary')

icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJUExURQAAAP+7AAAAAACwewkAAAADdFJOU///ANfKDUEAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQ+SURBVHhe1ZhJkttIEAQ1+v+jx5ogkZGeW6HYoFF+EipjG2kOUv/5u8kfwPsqiXGKY7VC7Uyw9FG+LoeeniBvclxNC50N1NYhWjBDdwmVRYY8L6P+GsrSCPd4AR+dQ1ES4J4ugvSEIKHffW/AfBIEDHgbFoB4Z0DFfw5eFTY44pX2BN9tUHdypLLpQfJKt4elhHoHq/IBzQS25dBlsKgakC9gTwe9L1h0YQArJug/YNHyAMavwIwfWFQMoG1vQLaATfkAuh4wfQVmpGV8KPp3FjAhXRCf6HnB+An6D9gWB9AhsKKF5hehj98dLKmhU2AhPh0MYk2JtwE04lNJktiUQhNAo/9S0jSWJcARfyd9pftQijxfFoH8ZXEPrlN/rVSJWpYAtRnc28KAJlRPAEqn1sd8gCpcLHP9UYCu+e+4OADRPB44yZNSkA3QuzPSnN0peNBp4gC90hkLhvMDavIF2QD6Hsg9iHj7Qe8ncucAOeVe1lTvT9RoqKIeQNcLkYgMrwdwGqLxA+Sw5H4K+fKERkNV1QB6FJHV0OQQnQ7YsJfQA0S5MWBeQENAtOkA6gMSEKA2xeQ2oM/Au4iBmoLNvx8kA6gWfXgAgy05nQPsJcqzm7ydOFNuS27zADl1C5yHguYYBlBbJlXvS2c7HQMarZxwzt5OnClK5LQ/4HlzLyedrR1A5ZRUMdns9BUD1pT5vWCyyW0Y4KN4rBlscnQDqJuTKiabHacBGsVTx2Cz6zjAtDz09LbzujDgqebjTGezTv1fsFLfgLYaVN0Jux9QdIHLdnY/oKgG6usB7w0I+vAwc5YqFFVQfz3hvQHBEB4WMI9AUUEwhIcFzCNQVBAM4WEB8wgUFQRDeFjAPAJFBcEQHhYwj0BRQTCEhwXMI1BUQAe/lxCTQVEBHfxeQkwGRQW0CZTW0HlAVQFtJxTWqGv+CwlRt4PCGvOs/I0oYA4HZQ1m+jcH5Aso6jDX9A+THLEYFDWIa29ANoGKDrEN/zitkYyrVvcnsD3AT+BtwIzTDyjuQQq/Y8Dun8E22j/9mO4OpO5bBnz4z8D1c8AHFkjZ1o/r32YYcPsC9H/LgM8tYH8y4NYF2uMGfOq3IPRnA25coC0Y8JnfgtifDrhtgXaEAR9YoA1We/7q9gWaL61fNODmBZqupcWAX1/gwosBdy5w0a5TP+5b4IJ9pfu6a4GLRSM+HczZxaei0X/essBnshDfWPALExAY+vjw2wsQx7ZkwO8uQBi70gFc8MYEJrGpGBAWbE5gSt7Fhwd0bi1gRlHFhwN6r0+gv+ivBiQLLk2gt+wvB6QTFjfQ9QPTT+pLumDeQP0Bs43mVCxoRlB3wmShuzUTwgpeFaY6+ms/YQ0mgun+9gLmkVHw3gRmRRYk+xOYk7Ek2pvAjJxF2fUNtFcsCy9NoLPhinZxAz09F+U/sFChdmbDcvB+9cH/Oj83tbCA5yUAAAAASUVORK5CYII="

icon_data = base64.b64decode(icon_base64)
image = Image.open(BytesIO(icon_data))
photo = ImageTk.PhotoImage(image)

window.iconphoto(False, photo)

window.configure(bg='white')

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(window, width=40, height=10, bg='white', fg='black',
               font=('Arial', 30), yscrollcommand=scrollbar.set)
text.pack(pady=20)

scrollbar.config(command=text.yview)

text.tag_configure('1', foreground='#FF0000')
text.tag_configure('2', foreground='#CC0033')
text.tag_configure('3', foreground='#990066')
text.tag_configure('4', foreground='#660099')
text.tag_configure('5', foreground='#3300CC')
text.tag_configure('6', foreground='#0000FF')
text.tag_configure('7', foreground='#0040BF')
text.tag_configure('8', foreground='#008080')
text.tag_configure('9', foreground='#00BF40')
text.tag_configure('10', foreground='#00FF00')


try:
    with open(path / 'mood_log.json', 'r') as file:
        lines = file.readlines()
        if not lines:
            text.insert(tk.END, "No mood data available.")
        else:
            for line in lines:
                data = json.loads(line.strip())
                date = data.get('date')
                mood = data.get('mood')
                text.configure(state ='normal')
                if mood == 1:
                    text.insert(tk.END, '■', '1')
                elif mood == 2:
                    text.insert(tk.END, '■', '2')
                elif mood == 3:
                    text.insert(tk.END, '■', '3')
                elif mood == 4:
                    text.insert(tk.END, '■', '4')
                elif mood == 5:
                    text.insert(tk.END, '■', '5')
                elif mood == 6:
                    text.insert(tk.END, '■', '6')
                elif mood == 7:
                    text.insert(tk.END, '■', '7')
                elif mood == 8:
                    text.insert(tk.END, '■', '8')
                elif mood == 9:
                    text.insert(tk.END, '■', '9')
                elif mood == 10:
                    text.insert(tk.END, '■', '10')
                text.configure(state ='disabled')
except FileNotFoundError:
    text.insert(tk.END, "Mood log file not found. Please log your mood first.") 

window.mainloop()