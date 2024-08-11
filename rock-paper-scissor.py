import tkinter as tk
from tkinter import font as tkfont
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        # Center the window on the screen
        self.center_window(400, 350)

        self.root.configure(bg="#f0f0f0")

        # Initialize statistics
        self.wins = 0
        self.losses = 0
        self.ties = 0

        # Create the GUI elements
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        # Title label
        title_font = tkfont.Font(family="Segoe UI", size=20, weight="bold")
        title_label = tk.Label(self.root, text="Rock-Paper-Scissors", font=title_font, bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=20)

        # Statistics frame
        stats_frame = tk.Frame(self.root, bg="#f0f0f0")
        stats_frame.pack(pady=10)

        self.stats_label = tk.Label(stats_frame, text="Wins: 0 | Losses: 0 | Ties: 0", font=("Segoe UI", 12), bg="#f0f0f0")
        self.stats_label.pack()

        # Buttons for Rock, Paper, Scissors
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"), font=("Segoe UI", 14), bg="#007bff", fg="white", relief="flat", width=10)
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"), font=("Segoe UI", 14), bg="#28a745", fg="white", relief="flat", width=10)
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"), font=("Segoe UI", 14), bg="#dc3545", fg="white", relief="flat", width=10)
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Result frame
        result_frame = tk.Frame(self.root, bg="#f0f0f0")
        result_frame.pack(pady=20)

        self.result_label = tk.Label(result_frame, text="", font=("Segoe UI", 14), bg="#f0f0f0")
        self.result_label.pack()

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = f"It's a tie! Computer chose {computer_choice.capitalize()}."
            self.ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = f"You win! Computer chose {computer_choice.capitalize()}."
            self.wins += 1
        else:
            result = f"You lose! Computer chose {computer_choice.capitalize()}."
            self.losses += 1

        self.result_label.config(text=result)
        self.update_statistics()

    def update_statistics(self):
        self.stats_label.config(text=f"Wins: {self.wins} | Losses: {self.losses} | Ties: {self.ties}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop() 
