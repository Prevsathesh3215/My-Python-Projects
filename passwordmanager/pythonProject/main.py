from tkinter import *
from tkinter import messagebox
import pyperclip, json


def display_exist_error():
    messagebox.showerror(title="Error", message="Website entry already exists!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def fill_password():
    import password
    entry_passwd.delete(0, END)
    password = password.generate_password()
    entry_passwd.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_passwd():
    website = entry_website.get()
    email = entry_email.get()
    pswd = entry_passwd.get()
    data_list = [website, email, pswd]

    if data_list[0] == '' or data_list[2] == '' or (data_list[0] == 0 and
            data_list[2] == ''):
        messagebox.showerror(title="Error", message="No data for email and password fields.")
    else:
        data_use = {website: {
            "email": email,
            "password": pswd,
        }}
        try:
            with open('data_file.json', 'r') as fd:
                # json.dump(data_use, fd, indent=4)
                data = json.load(fd)
                for x in data:
                    if website == x:
                        display_exist_error()
                    else:
                        data.update(data_use)

        except:
            with open('data_file.json', 'w') as fd:
                json.dump(data_use, fd, indent=4)

        else:
            with open('data_file.json', 'w') as fd:
                json.dump(data, fd, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_passwd.delete(0, END)


def search_entry():

    website = entry_website.get()
    with open("data_file.json", "r") as fd:
        data = json.load(fd)

        try:
            data_email = data[website]["email"]
            data_pswd = data[entry_website.get()]["password"]
        except KeyError:
            messagebox.showerror(title="Error", message="Data does not exist")

        else:
            messagebox.showinfo(title=entry_website.get(), message=
                                f"Email: {data_email}\nPassword: {data_pswd}")



# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Password Manager')
root.minsize(700,  500)


label_website = Label(text="Website:")
label_website.place(x=100, y=280)
entry_website = Entry(width=30, relief=FLAT)
entry_website.place(x=200, y=280)
entry_website.focus()

button_search = Button(text="Search", relief=GROOVE, bg="white", width=22,
                       command=search_entry)
button_search.place(x=400, y=275)

label_email = Label(text="Email/Username:")
label_email.place(x=80, y=305)
entry_email = Entry(width=60, relief=FLAT)
entry_email.place(x=200, y=305)
entry_email.insert(END, "prevsathesh3215@gmail.com")


label_passwd = Label(text='Password:')
label_passwd.place(x=90, y=330)
entry_passwd = Entry(width=30, relief=FLAT)
entry_passwd.place(x=200, y=330)
fill_password()

button_generate = Button(text="Generate Password", relief=GROOVE,
                         width=20, bg="white", command=fill_password)
button_generate.place(x=415, y=330)
button_add = Button(text="Add", relief=GROOVE, width=51, bg="white",
                    command=save_passwd)
button_add.place(x=200, y=360)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.place(x=250, y=50)


root.mainloop()
