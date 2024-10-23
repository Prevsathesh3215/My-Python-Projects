from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Password Manager')
root.minsize(700,  500)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
canvas.config()

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

entry_website = Entry(width=60, relief=FLAT)
entry_website.grid(row=1, column=1, columnspan=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = Entry(width=60, relief=FLAT)
entry_email.grid(row=2, column=1, columnspan=2)

label_passwd = Label(text='Password:')
label_passwd.grid(row=3, column=0)

entry_passwd = Entry(width=30, relief=FLAT)
entry_passwd.grid(row=3, column=1)

button_generate = Button(text="Generate Password", relief=GROOVE,\
                         width=20, bg="white")
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", relief=GROOVE, width=51, bg="white")
button_add.grid(row=4, column=0, columnspan=4)



root.mainloop()