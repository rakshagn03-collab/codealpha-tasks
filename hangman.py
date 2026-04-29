import random
import tkinter as tk

# Optional sound (safe fallback)
try:
    import winsound
    def play_correct():
        winsound.Beep(1000, 150)
    def play_wrong():
        winsound.Beep(400, 300)
except:
    def play_correct():
        pass
    def play_wrong():
        pass


# Words list
words = ["python", "india", "laptop", "science", "engineer"]
word = random.choice(words)

guessed = []
wrong = 0
max_attempts = 6

# ASCII stages
stages = [
"""
   -----
   |   |
       |
       |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
"""
]

# Update word display
def update_display():
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)

# Update hangman drawing
def update_hangman():
    hangman_label.config(text=stages[wrong])

# Guess logic
def guess_letter():
    global wrong

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        result_label.config(text="⚠️ Enter a single valid letter!")
        return

    if letter in guessed:
        result_label.config(text="⚠️ Already guessed!")
        return

    guessed.append(letter)

    if letter in word:
        play_correct()
        result_label.config(text="✅ Correct!")
    else:
        wrong += 1
        play_wrong()
        result_label.config(text=f"❌ Wrong! Attempts left: {max_attempts - wrong}")

    update_display()
    update_hangman()

    if all(l in guessed for l in word):
        result_label.config(text=f"🎉 You Win! Word: {word}")

    if wrong == max_attempts:
        result_label.config(text=f"💀 Game Over! Word: {word}")

# Restart game
def restart_game():
    global word, guessed, wrong
    word = random.choice(words)
    guessed = []
    wrong = 0
    result_label.config(text="")
    update_display()
    update_hangman()

# GUI setup
root = tk.Tk()
root.title("🎮 Hangman Game")

# Hangman drawing
hangman_label = tk.Label(root, text=stages[0], font=("Courier", 12), justify="left")
hangman_label.pack()

# Word display
word_label = tk.Label(root, text="_ " * len(word), font=("Arial", 20))
word_label.pack(pady=10)

# Input
entry = tk.Entry(root)
entry.pack()

# Buttons
guess_btn = tk.Button(root, text="Guess", command=guess_letter)
guess_btn.pack(pady=5)

restart_btn = tk.Button(root, text="Restart", command=restart_game)
restart_btn.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Initialize
update_display()
update_hangman()

# Run
root.mainloop()