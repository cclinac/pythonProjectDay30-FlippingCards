import tkinter as tk
BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_image = tk.PhotoImage(file="./images/card_front.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                         bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)

wrong_image = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                         bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

window.mainloop()