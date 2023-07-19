from tkinter import *
import requests

COUNT = 10
score = 0

window = Tk()
window.title("Typing Speed Analyser")
window.minsize(height=600, width=600)

sample_text = ""
response = requests.get(url="https://random-word-api.herokuapp.com/word?number=100")
words = response.json()
for word in words:
    sample_text += word + " "


def start_timer():
    global score
    score = 0
    count_down(COUNT - 1)
    type_text.config(state='normal')
    type_text.delete(0, END)
    score_text.destroy()
    canvas.itemconfig(timer_text, fill='green')


def count_down(count):
    count_second = count
    if count < 10:
        count_second = f"0{count}"
    canvas.itemconfig(timer_text, text=f"0:{count_second}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        type_text.config(state='disabled')
        typed_words = type_text.get().split()
        result(typed_words)
        canvas.itemconfig(timer_text, text="Time's Up!", fill='red')


def result(typed_words):
    # print(typed_words)
    global sample_words, score
    for word in typed_words:
        if word in sample_words:
            score += 1

    global score_text
    score_text = Label(text=f"You typed {score} words! => WPM: {score}", fg='green')
    score_text.grid(padx=10, pady=10, row=5, column=1)


start_timer = Button(text='Start', command=start_timer)
start_timer.grid(row=0, column=1, pady=10)

canvas = Canvas(height=60, width=60)
timer_text = canvas.create_text(30, 30, text="1:00", fill='green')
canvas.grid(row=1, column=1, pady=10, padx=10)

text_sample = Text(window, height=12, width=70)
text_sample.insert(END, sample_text)
text_sample.config(padx=5)
text_sample.grid(row=2, column=1, pady=10, padx=20)

sample_words = text_sample.get('1.0', END)

label = Label(text='Type the sample text given above', font=('Arial', 10, 'normal'))
label.grid(row=3, column=1, padx=10, pady=10)

type_text = Entry(width=90)
type_text.config(state='disabled')
type_text.grid(row=4, column=1)

window.mainloop()

