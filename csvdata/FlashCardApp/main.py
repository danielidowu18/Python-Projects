from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
data_dict = []

# Reading data files
try:
    data = pandas.read_csv("./FlashCardApp/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./FlashCardApp/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def new_card():
    window.after_cancel(flip_timer)
    new_word()


def canv_func():
    global card_canvas, canvas_image, canvas_text, canvas_title
    card_canvas = Canvas(width=800, height=527, highlightthickness=0, bg=BACKGROUND_COLOR)
    canvas_image = card_canvas.create_image(400, 263, image=card_image)
    card_canvas.grid(row=0, column=0, columnspan=2)
    canvas_title = card_canvas.create_text(400, 200, text="", font=("Arial", 30, "italic"))
    canvas_text = card_canvas.create_text(400, 263, text="", font=("Arial", 30, "bold"))
    
    
# Creating a new file with updated words
def unknown_words_file():
    data_dict.remove(current_word)
    df = pandas.DataFrame(data_dict)
    df.to_csv("./FlashCardApp/words_to_learn.csv", index=False)
    new_card()


def new_word():
    global current_word, flip_timer
    canv_func()
    current_word = random.choice(data_dict)
    french_word = current_word["French"]
    card_canvas.itemconfig(canvas_title, text=f"French")
    card_canvas.itemconfig(canvas_text, text=f"{french_word}")
    flip_timer = window.after(3000, flip_card)

    
def flip_card():    
    english_word = current_word["English"]
    card_canvas.itemconfig(canvas_image, image=card_front)
    card_canvas.itemconfig(canvas_title, text=f"English", fill="white")
    card_canvas.itemconfig(canvas_text, text=f"{english_word}", fill="white")


# UI setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_image = PhotoImage(file="./FlashCardApp/card_front.png")
card_front = PhotoImage(file="./FlashCardApp/card_back.png")


# Buttons in setup
left_image = PhotoImage(file="./FlashCardApp/wrong.png")
left_button = Button(image=left_image, bg=BACKGROUND_COLOR, border=0, command=new_card)
left_button.grid(row=1, column=0)

right_image = PhotoImage(file="./FlashCardApp/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, border=0, command=unknown_words_file)
right_button.grid(row=1, column=1)


new_word()


window.mainloop()