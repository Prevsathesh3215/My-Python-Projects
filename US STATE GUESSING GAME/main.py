from turtle import *

import pandas
import pandas as p

screen = Screen()
writing = Turtle()
writing.pu()
writing.hideturtle()

screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
shape(image)

datafile = p.read_csv("50_states.csv")
datadict = datafile.to_dict()
guessed = []


while len(guessed) < 50:

    ans = screen.textinput(title="Guess the State", prompt="What's another " \
                                                           "state name?")
    if ans == "Exit":
        break

    else:
        for i in datadict['state']:
            if datadict['state'][i] == ans:
                guessed.append(ans)
                writing.goto((datadict['x'][i], datadict['y'][i]))
                writing.write(datadict['state'][i], align="center", font=  ("Arial", 8, "normal"))


for state in guessed:
    datafile = datafile.drop(datafile[datafile["state"] == state].index)


datafile.to_csv("states to learn.csv")



