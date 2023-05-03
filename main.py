from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARDS MANAGER ------------------------------- #


def new_card():
    """Picks a random word in French from the dictionary and creates a new card."""
    global flip_timer
    window.after_cancel(flip_timer)
    random_word_pair = random.choice(list(french_english_dict["data"]))
    random_french_word = random_word_pair[0]

    front_canvas = Canvas(height=580, width=890, background=BACKGROUND_COLOR, highlightthickness=0)
    front_canvas.create_image(460, 290, image=card_front_img)
    front_canvas.create_text(450, 150, text="French", fill="black", font=("Courier", 40, "italic"))
    front_canvas.create_text(450, 263, text=random_french_word, fill="black", font=("Courier", 60, "bold"))
    front_canvas.grid(row=0, column=0, columnspan=2)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Shows English translation of a randomly picked French word."""
    random_word_pair = random.choice(list(french_english_dict["data"]))
    english_translation = random_word_pair[1]

    back_canvas = Canvas(height=580, width=890, background=BACKGROUND_COLOR, highlightthickness=0)
    back_canvas.create_image(460, 290, image=card_back_img)
    back_canvas.create_text(450, 150, text="English", fill="white", font=("Courier", 40, "italic"))
    back_canvas.create_text(450, 263, text=english_translation, fill="white", font=("Courier", 60, "bold"))
    back_canvas.grid(row=0, column=0, columnspan=2)


# ---------------------------- READ DICTIONARY ------------------------------- #


data = pandas.read_csv("data/french_words.csv")
french_english_dict = data.to_dict(orient="tight")


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Flash Cards")
window.minsize(width=800, height=720)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Canvas

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

# Buttons

check_button_img = PhotoImage(file="images/right.png")
cross_button_img = PhotoImage(file="images/wrong.png")

check_button = Button(padx=50, image=check_button_img, highlightthickness=0, command=new_card)
check_button.grid(row=1, column=1)

cross_button = Button(padx=50, image=cross_button_img, highlightthickness=0, command=new_card)
cross_button.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)
new_card()


window.mainloop()
