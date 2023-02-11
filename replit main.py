# Screen Resolution 1024 * 600

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar
from rounded_button import RoundedButton

window = tk.Tk()
window.title("PhotoBooth UI")
window_width = 1024
window_height = 600
window.geometry("%dx%d" % (window_width, window_height))

countdown_timer_amount = 5

white_image = ImageTk.PhotoImage(Image.open("white.png"))
white_image_label = tk.Label(image=white_image)
white_image_label.image = white_image

last_image_taken= ImageTk.PhotoImage(Image.open("red_panda.png"))
last_image_taken_label = tk.Label(image=last_image_taken)
last_image_taken_label.image = last_image_taken



image = Image.open("yes.png")
bg_image = ImageTk.PhotoImage(image)

image_label = tk.Label(image=bg_image)
image_label.image = bg_image
image_label.place(x=0, y=0)




def show_gui():
  print('show gui')
  image_label.place(x=0, y=0)
  
  next_filter_button.place(x=next_filter_button_x,   y=next_filter_button_y)
  prev_filter_button.place(x=prev_filter_button_x, y=prev_filter_button_y)
  next_background_button.place(x=next_background_button_x, y=next_background_button_y)
  prev_background_button.place(x=prev_background_button_x, y=prev_background_button_y)
  capture_button.place(x=capture_button_x, y=capture_button_y)
  countdown_label.place_forget()
  white_image_label.place_forget()
  last_image_taken_label.place_forget()


  
def hide_gui():
  print('hide gui')
  capture_button.place_forget()
  prev_background_button.place_forget()
  next_background_button.place_forget()
  prev_filter_button.place_forget()
  next_filter_button.place_forget()


def show_flash():
  print('flash')
  image_label.place_forget()
  countdown_label.place_forget()
  white_image_label.place(x=0, y=0)
  window.after(100, hide_flash)


def hide_flash():
  print('hide flash')
  white_image_label.place_forget()
  last_image_taken_label.place(x=0, y=0)
  window.after(1000, show_gui)
  


def change_countdown_label(seconds):
  print('called', seconds)
  if seconds > 0:
    countdown_label_text.set(seconds)
    window.after(1000, lambda : change_countdown_label (seconds - 1))
  else:
    take_photo()


def take_photo():
  #TODO: take a picture using opencv
  show_flash()


  
def capture_photo():
  hide_gui()
  countdown_label.place(x=countdown_label_x, y=countdown_label_y)
  change_countdown_label(countdown_timer_amount)

  
# button stuff
button_width = 125
button_height = 50
pixel = tk.PhotoImage(width=1, height=1)
capture_button_width = 550
capture_button_height = 50
padding = 100

# capture button section
capture_button_x = window_width / 2 - capture_button_width / 2
capture_button_y = window_height * 0.8


capture_button = RoundedButton(
  text="Capture", 
  radius=45, 
  btnbackground="#029510", 
  btnforeground="#ffffff", 
  clicked=capture_photo, 
  width=capture_button_width, 
  height=capture_button_height)

# capture_button = tk.Button(
#     text="Capture",
#     image=pixel,
#     width=button_width,
#     height=button_height,
#     compound="c",
#     command=capture_photo,
#     font=("Arial", 10,"bold"),
#     fg="black",
#     bg="#4286f4",
#     activebackground="#0066cc",
#     activeforeground="white"
# )

# Prev background button section
prev_background_button_x = padding
prev_background_button_y = padding

prev_background_button = tk.Button(
    text="Prev Background",
    image=pixel,
    width=button_width,
    height=button_height,
    compound="c"
)

# next Background button section
next_background_button_x = window_width - button_width - padding
next_background_button_y = padding

next_background_button = tk.Button(
    text="Next Background",
    image=pixel,
    width=button_width,
    height=button_height,
    compound="c"
)

# Prev filter button section
prev_filter_button_x = padding
prev_filter_button_y = window_height - button_height - padding

prev_filter_button = tk.Button(
    text="Prev Filter",
    image=pixel,
    width=button_width,
    height=button_height,
    compound="c"
)

# Next Filter button section
next_filter_button_x = window_width - button_width - padding
next_filter_button_y = window_height - button_height - padding

next_filter_button = tk.Button(
    text="Next Filter",
    image=pixel,
    width=button_width,
    height=button_height,
    compound="c"
)


# countdown label section
countdown_label_text = StringVar()
countdown_label_text.set(str(countdown_timer_amount),)

countdown_label_x = window_width / 2 - button_width / 2
countdown_label_y = window_height / 2 - button_height / 2

countdown_label = tk.Label(
  textvariable=countdown_label_text,
  image=pixel,
  width=button_width,
  height=button_height,
  compound="c"
)


show_gui()
tk.mainloop()

