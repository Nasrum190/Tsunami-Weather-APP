from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=46977cd74469b505340974987a860119").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    r_temp=round(data["main"]["temp"]-273.15,2)
    temp_label1.config(text=str(r_temp))
    pres_label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("Weather App")
win.config(bg = "#ADD8E6" )
win.geometry("500x570")


bg_image = Image.open("WeatherAPP.jpg")
bg_image = bg_image.resize((500, 570), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(win, width=500, height=570)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")



name_label=Label(win, text='Tsunami Weather App',
                 font=("Times New Roman", 30 , "bold"))
name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
 'West Virginia', 'Wisconsin', 'Wyoming']

com=ttk.Combobox(win, text='Tsunami Weather App',values=list_name,
                 font=("Times New Roman", 15 , "bold"), textvariable=city_name)

com.place(x=80,y=120,height=50,width=350)


w_label=Label(win, text='Weather Climate', font=("Times New Roman", 17))
w_label.place(x=25,y=260,height=50, width=210)
w_label1=Label(win, text='', font=("Times New Roman", 17))
w_label1.place(x=250,y=260,height=50, width=210)


wd_label=Label(win, text='Weather Description', font=("Times New Roman", 17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1=Label(win, text='', font=("Times New Roman", 17))
wd_label1.place(x=250,y=330,height=50,width=210)


temp_label=Label(win, text='Temperature (°C)', font=("Times New Roman", 17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win, text='', font=("Times New Roman", 17))
temp_label1.place(x=250,y=400,height=50,width=210)


pres_label=Label(win, text='Pressure', font=("Times New Roman", 17))
pres_label.place(x=25,y=470,height=50,width=210)
pres_label1=Label(win, text='', font=("Times New Roman", 17))
pres_label1.place(x=250,y=470,height=50,width=210)


button = Button(win, text='Search', font=("Times New Roman", 17 , "bold"),command=data_get)
button.place(x=200, y=190, height=50 , width=100)

win.mainloop()
