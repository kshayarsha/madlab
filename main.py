from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ''

# UI setup
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tom)
timertext = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, '24', 'bold'))
canvas.grid(row=1, column=1)

check = Label(text='', fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)


def countdown(count):
    global reps
    if count == 0:
        if reps % 2 == 0 and reps < 10:
            canvas.create_text(100, 100, text='Work', fill='white', font=(FONT_NAME, '24', 'bold'))
            countdown(WORK_MIN)
        elif reps % 2 == 1 and reps < 9:
            canvas.create_text(100, 100, text='Short break', fill='white', font=(FONT_NAME, '24', 'bold'))
            countdown(SHORT_BREAK_MIN * 60)
        elif reps % 8 == 0:
            canvas.create_text(100, 100, text='Long break', fill='white', font=(FONT_NAME, '24', 'bold'))
            countdown(LONG_BREAK_MIN * 60)
        reps += 1
        print(reps)
        if reps % 2 == 0:
            global marks
            marks = check.config(text='✔' * (reps // 2))
    else:
        x = count // 60
        y = count % 60
        x = str(x).zfill(2)
        y = str(y).zfill(2)
        clock = x + ':' + y
        canvas.itemconfig(timertext, text=clock)
        global timer
        timer = window.after(1000, countdown, count - 1)


def clicked():
    global reps
    if reps % 2 == 0 and reps < 10:
        lab = canvas.create_text(100, 100, text='Work', fill='white', font=(FONT_NAME, '24', 'bold'))
        countdown(15)
    elif reps % 2 == 1 and reps < 9:
        lab = canvas.create_text(100, 100, text='Short break', fill='white', font=(FONT_NAME, '24', 'bold'))
        countdown(300)
    elif reps % 8 == 0:
        lab = canvas.create_text(100, 100, text='Long break', fill='white', font=(FONT_NAME, '24', 'bold'))
        countdown(900)


def clicker():
    window.after_cancel(timer)
    canvas.itemconfig(timertext, text='00:00')
    marks = ''
    global reps
    reps = 0


start = Button(text='start', highlightthickness=0, command=clicked)
start.grid(row=2, column=0)

reset = Button(text='reset', highlightthickness=0, command=clicker)
reset.grid(row=2, column=2)

check = Label(text='✔', fg=GREEN, bg=YELLOW)

window.mainloop()
