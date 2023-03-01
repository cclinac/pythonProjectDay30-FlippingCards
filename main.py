import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pd.pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_counter
    window.after_cancel(flip_counter)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_counter = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(background_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_image = tk.PhotoImage(file="./images/card_front.png")
card_back_image = tk.PhotoImage(file="./images/card_back.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
background_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                         bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=0)

wrong_image = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                         bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

flip_counter = window.after(3000, flip_card)
next_card()



window.mainloop()
