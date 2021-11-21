# (C)opyright 2021 Edward Francis Westfield Jr.
# https://edwestfieldjr.com/
# MIT License
# Note: This project was created for a class: 100 Days of Code:
# The Complete Python Pro Bootcamp for 2022
# https://www.udemy.com/course/100-days-of-code/
# Day 85, Assignment 5: Typing Speed Test
# https://www.udemy.com/course/100-days-of-code/learn/practice/1251152


import time
from tkinter import *

PROJECT_APP_NAME = "The Typing Speed App"
PROJECT_HEADING = "Type below in English"
PROJECT_WINDOW_TITLE = "The Typing Speed App"


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main_text = str()
        self.nanosecond_array = list()
        self.create_interface()
        self.grid()

    def create_interface(self):
        title_config = {'bg': 'red', 'fg': 'white'}
        self.heading_label = Label(text=PROJECT_APP_NAME, font=("Arial", 36, "bold"), cnf=title_config)
        self.heading_label.grid(row=0, column=0, columnspan=2)

        self.text_label = Label(
            text="Type a complete sentence or passage below.\nWhen finished, hit “Check Speed”.\nSpeed will then display above.\nHit “Clear/Reset” to start over.",
            font=("Arial", 14))
        self.text_label.grid(row=1, column=0, columnspan=2)

        self.text_entry = Text()
        self.text_entry.grid(row=2, column=0, columnspan=2)
        self.text_entry.bind('<KeyPress>', self.check_input_for_key)

        self.make_button = Button(text="Clear/Reset", bg="#dddddd", highlightbackground="#dddddd", fg="black",
                                  command=lambda: self.clear())
        self.make_button.grid(row=3, column=0, columnspan=1)

        self.make_button = Button(text="Check Speed", bg="#dddddd", highlightbackground="#dddddd", fg="black",
                                  command=lambda: self.check_speed())
        self.make_button.grid(row=3, column=1, columnspan=1)

    def check_input_for_key(self, key):
        self.main_text = self.text_entry.get("1.0", "end-1c")
        self.nanosecond_array.append(time.time_ns())
        print(self.main_text)
        print(self.nanosecond_array)

    def check_speed(self):
        if self.main_text and len(self.nanosecond_array) > 1:
            estimated_word_count = len(self.main_text) / 5
            typing_time_in_minutes = ((self.nanosecond_array[-1] - self.nanosecond_array[0]) / 1000000000) / 60
            self.typing_speed_wpm = estimated_word_count / typing_time_in_minutes
            print(estimated_word_count, typing_time_in_minutes, self.typing_speed_wpm)
            self.heading_label.config(text=f"{int(self.typing_speed_wpm)} wpm")
            self.reset_input()
            return self.typing_speed_wpm

    def clear(self):
        print("clear")
        self.heading_label.config(text=PROJECT_APP_NAME)
        self.reset_input()

    def reset_input(self):
        self.text_entry.delete('1.0', END)
        self.main_text = " "
        self.nanosecond_array = []


root = Tk()
root.title(PROJECT_WINDOW_TITLE)
app = Application(master=root)
app.mainloop()
