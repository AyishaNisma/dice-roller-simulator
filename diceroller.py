import tkinter as tk
import random

# Dice face unicode characters (can be replaced with images if needed)
dice_faces = {
    1: "\u2680",  # ⚀
    2: "\u2681",  # ⚁
    3: "\u2682",  # ⚂
    4: "\u2683",  # ⚃
    5: "\u2684",  # ⚄
    6: "\u2685"   # ⚅
}

def roll_dice():
    number = random.randint(1, 6)
    dice_label.config(text=dice_faces[number], font=("Helvetica", 100))
    result_label.config(text=f"You rolled a {number}!")

# Create main window
root = tk.Tk()
root.title("Dice Roller Simulator")
root.geometry("300x300")
root.resizable(False, False)

# Dice output label
dice_label = tk.Label(root, text="", font=("Helvetica", 100))
dice_label.pack(pady=20)

# Result text
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

# Roll button
roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
