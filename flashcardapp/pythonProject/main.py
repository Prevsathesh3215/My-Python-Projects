from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    data_file = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("french_words.csv")

data_dict = data_file.to_dict()
key_ref = [i for i in data_dict["French"]]
random_word = random.randrange(1, 100)


root = Tk()
root.title("Flashcard App")
root.minsize(width=1000, height=690)
root.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=750, bg=BACKGROUND_COLOR,
                highlightthickness=0)
bg_img = PhotoImage(file="card_back.png")
fg_img = PhotoImage(file="card_front.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")


def run_french():
    global word_choice
    word_choice = random.choice(key_ref)
    print("Run French :" + str(word_choice))
    canvas.create_image(400, 290, image=fg_img)

    canvas.create_text(400, 160, text="French", fill='black',
                       font=('Arial', 35, 'italic'))
    canvas.create_text(400, 300, text=data_dict["French"][word_choice], fill='black',
                       font=('Arial', 35, 'bold'))
    canvas.place(x=100, y=10)
    canvas.after(3000, run_english)


def run_english():
    canvas.delete('all')
    canvas.create_image(400, 300, image=bg_img)
    canvas.create_text(400, 160, text="English", fill='white',
                       font=('Arial', 35, 'bold'))
    canvas.create_text(400, 300, text=data_dict["English"][word_choice], fill='white',
                       font=('Arial', 35, 'bold'))


def remove_word():
    print("Remove word: " + str(word_choice))
    data_dict["French"].pop(word_choice)
    data_dict["English"].pop(word_choice)
    key_ref.remove(word_choice)

    run_french()


right_button = Button(image=right_img, borderwidth=0, highlightthickness=0,
                      activebackground=BACKGROUND_COLOR, command=remove_word)
right_button.grid(row=1, column=2)
right_button.place(x=600, y=570)

wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0,
                      activebackground=BACKGROUND_COLOR, command=run_french)
wrong_button.grid(row=1, column=0)
wrong_button.place(x=300, y=570)

run_french()


root.mainloop()

df = pandas.DataFrame(data_dict)
df.to_csv('words_to_learn.csv', index=False)