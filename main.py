import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pd.pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_image = tk.PhotoImage(file="./images/card_front.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front_image)
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

next_card()
window.mainloop()
