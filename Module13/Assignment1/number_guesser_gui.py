import random
import tkinter as tk
import unittest

class NumberGuesser:
    guessed_list = []

    @classmethod
    def add_guess(cls, guess):
        cls.guessed_list.append(guess)

class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        NumberGuesser.guessed_list = []

    def test_constructor(self):
        self.assertEqual(len(NumberGuesser.guessed_list), 0)

    def test_adding_to_guessed_list(self):
        NumberGuesser.add_guess(1)
        NumberGuesser.add_guess(2)
        self.assertEqual(len(NumberGuesser.guessed_list), 2)
        self.assertEqual(NumberGuesser.guessed_list[0], 1)
        self.assertEqual(NumberGuesser.guessed_list[1], 2)

    def tearDown(self):
        NumberGuesser.guessed_list = []
class NumberGuessingGame:
    def __init__(self, max_num):
        self.max_num = max_num
        self.secret_number = None
        self.guesses = []
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("400x400")
        self.window.resizable(False, False)
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.num_buttons = []
        for i in range(1, self.max_num + 1):
            button = tk.Button(self.window, text=str(i), command=lambda num=i: self.make_guess(num))
            button.grid(row=(i-1)//5, column=(i-1)%5)
            self.num_buttons.append(button)
        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.grid(row=self.max_num//5+1, column=0, columnspan=5)
        self.reset_button = tk.Button(self.window, text="Reset Game", command=self.reset_game, state="disabled")
        self.reset_button.grid(row=self.max_num//5+2, column=0, columnspan=5)
        self.result_label = tk.Label(self.window, text="", font=("Arial", 24))
        self.result_label.grid(row=self.max_num//5+3, column=0, columnspan=5)

    def start_game(self):
        self.secret_number = random.randint(1, self.max_num)
        self.guesses = []
        for button in self.num_buttons:
            button.configure(state="normal")
        self.reset_button.configure(state="normal")
        self.result_label.configure(text="")

    def make_guess(self, num):
        if num == self.secret_number:
            self.result_label.configure(text="Winner!")
            NumberGuesser.add_guess(num)
            self.reset_game()
        else:
            self.num_buttons[num-1].configure(state="disabled")
            NumberGuesser.add_guess(num)
            self.guesses.append(num)
            if len(self.guesses) == self.max_num:
                self.result_label.configure(text="You lose!")
                self.reset_game()

    def reset_game(self):
        self.secret_number = None
        self.guesses = []
        for button in self.num_buttons:
            button.configure(state="disabled")
        self.start_button.configure(state="normal")
        self.reset_button.configure(state="disabled")



game = NumberGuessingGame(20)