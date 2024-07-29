import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Title label
        tk.Label(self.root, text="Rock Paper Scissors Game", font=('Arial', 20, 'bold')).pack(pady=10)

        # Instructions label
        tk.Label(self.root, text="Choose Rock, Paper, or Scissors to play against the computer.", font=('Arial', 14)).pack(pady=10)

        # User choice buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Rock", command=lambda: self.make_choice("Rock"), width=10, height=2).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Paper", command=lambda: self.make_choice("Paper"), width=10, height=2).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Scissors", command=lambda: self.make_choice("Scissors"), width=10, height=2).grid(row=0, column=2, padx=5)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=('Arial', 16))
        self.result_label.pack(pady=20)

        # Reset button
        tk.Button(self.root, text="Play Again", command=self.reset_game, font=('Arial', 12), width=15).pack(pady=10)

    def make_choice(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)

        # Update result label
        self.result_label.config(
            text=f"Computer chose: {computer_choice}\n{result}",
            fg="green" if "win" in result.lower() else "red"
        )

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a draw!"

        if (user_choice == "Rock" and computer_choice == "Scissors") or \
           (user_choice == "Paper" and computer_choice == "Rock") or \
           (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"

        return "You lose!"

    def reset_game(self):
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
