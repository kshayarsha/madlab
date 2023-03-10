from tkinter import *
from tkinter import messagebox

import password
from password import Password
import pyperclip
import json
import os


def click(website=None, pasword=None):
    newdat = {
        webentry.get(): {
            'email': userentry.get(),
            'password': pasentry.get()
        }
    }
    try:
        with open('data.json', 'r') as data:
            dat = json.load(data)
    except FileNotFoundError:
        with open('data.json', 'w') as datas:
            json.dump(newdat, datas, indent=4)
    else:
        dat.update(newdat)

        with open('data.json', 'w') as datfile:
            json.dump(dat, datfile, indent=4)

        if len(webentry.get()) == 0 or len(pasentry.get()) == 0:
            messagebox.askokcancel(title='oops', message='You left a field entry, please fill it')
        else:
            choice = messagebox.askokcancel(title=webentry.get(),
                                            message=f'is this correct \n Email: {userentry.get()} \n password: {pasentry.get()}')
            if choice == 1:
                webentry.delete(0, END)
                userentry.delete(0, END)
                userentry.insert(0, 'vedantarya.agrawal@gmail.com')
                pasentry.delete(0, END)


def make():
    s = pa.makepass()
    pyperclip.copy(s)
    pasentry.insert(0, s)


def findpas():
    websit = webentry.get()
    with open('data.json') as data_file:
        dat = json.load(data_file)
        if websit in dat.keys():
            email = dat[websit]['email']
            pasd = dat[websit]['password']
            messagebox.showinfo(title=websit, message=f'Email={email}\n password={pasd}')
        else:
            messagebox.showinfo(title='website not found', message='Website does not exist')


pa = Password()
window = Tk()

window.config(padx=50, pady=20)
window.title('Password Manager')
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web = Label(text='Website: ')
web.grid(row=1, column=0)
user = Label(window, text='E-mail/Username: ')
user.grid(row=2, column=0)
pas = Label(window, text='Password: ')
pas.grid(row=3, column=0)

webentry = Entry(width=21)
webentry.grid(row=1, column=1)
webentry.focus()
userentry = Entry(width=35)
userentry.grid(row=2, column=1, columnspan=2)
userentry.insert(0, 'vedantarya.agrawal@gmail.com')
pasentry = Entry(width=21)
pasentry.grid(row=3, column=1)

search = Button(text='Search', width=13, command=findpas)
search.grid(row=1, column=2)
gen = Button(text='Generate Password', command=make)
gen.grid(row=3, column=2)
ad = Button(text='Add', width=40, command=click)
ad.grid(row=4, column=1)

window.mainloop()
