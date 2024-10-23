# from tkinter import *
# import requests as rq
#
#
# def get_quote():
#     pass
#     resp = rq.get(url='https://api.kanye.rest')
#     data =  resp.json()
#     return data['quote']
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()

from tkinter import *
from turtle import *
import math


screen = Screen()
bob = Turtle()

screen.setup(1200, 546)
screen.bgpic('world_map2.png')
d = 10.5761
pixel_loc = (546 / (2 * math.pi) * math.log(math.tan(math.tan((((((math.pi)/4) + (d / 2)) * (math.pi) / 180))))))
bob.setpos((0, -23.5726))


screen.mainloop()