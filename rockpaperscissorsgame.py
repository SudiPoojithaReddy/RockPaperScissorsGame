import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        self.choices = ["Rock", "Paper", "Scissors"]

        # Create widgets
        self.user_label = tk.Label(master, text="Your Choice:")
        self.user_label.grid(row=0, column=0, padx=10, pady=10)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set(self.choices[0])  # Default choice
        self.user_choice_menu = tk.OptionMenu(master, self.user_choice_var, *self.choices)
        self.user_choice_menu.grid(row=0, column=1, padx=10, pady=10)

        self.play_button = tk.Button(master, text="Play", command=self.play_game)
        self.play_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, pady=10)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)

        result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

        if user_choice == computer_choice:
            result_text += "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result_text += "You Win!"
        else:
            result_text += "Computer Wins!"

        self.result_label.config(text=result_text)
        messagebox.showinfo("Result", result_text)

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
