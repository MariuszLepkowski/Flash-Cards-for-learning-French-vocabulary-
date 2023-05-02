from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARDS MANAGER ------------------------------- #


def flip_card():
    """Flips card and shows the english meaning of a word after three seconds"""
    pass


def new_card():
    """Picks new card with a random word in French."""
    print("New card")


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Flash Cards")
window.minsize(width=800, height=720)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Canvas

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

back_canvas = Canvas(height=580, width=890, background=BACKGROUND_COLOR, highlightthickness=0)
back_canvas.create_image(460, 290, image=card_back_img)
back_canvas.create_text(450, 150, text="English", fill="white", font=("Courier", 40, "italic"))
back_canvas.create_text(450, 263, text="Word", fill="white", font=("Courier", 60, "bold"))
back_canvas.grid(row=0, column=0, columnspan=2)

front_canvas = Canvas(height=580, width=890, background=BACKGROUND_COLOR, highlightthickness=0)
front_canvas.create_image(460, 290, image=card_front_img)
front_canvas.create_text(450, 150, text="French", fill="black", font=("Courier", 40, "italic"))
front_canvas.create_text(450, 263, text="Word", fill="black", font=("Courier", 60, "bold"))
front_canvas.grid(row=0, column=0, columnspan=2)


# Buttons

check_button_img = PhotoImage(file="images/right.png")
cross_button_img = PhotoImage(file="images/wrong.png")

check_button = Button(padx=50, image=check_button_img, highlightthickness=0, command=new_card)
check_button.grid(row=1, column=1)

cross_button = Button(padx=50, image=cross_button_img, highlightthickness=0, command=new_card)
cross_button.grid(row=1, column=0)


window.mainloop()
