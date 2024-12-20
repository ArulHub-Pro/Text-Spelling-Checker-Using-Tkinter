import tkinter as tk
from spellchecker import SpellChecker

# Initialize spellchecker
spell = SpellChecker()

# Functions
def check_text():
    """Checks the text for spelling issues and displays the corrected sentence."""
    text = user_input.get()
    if not text.strip():
        result_label.config(text="Please enter some text to check!", fg="red")
        return

    # Split text into words and find misspelled ones
    words = text.split()
    misspelled = spell.unknown(words)
    
    corrected_text = []
    for word in words:
        if word in misspelled:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    
    # Join the corrected words back into a sentence
    corrected_sentence = ' '.join(corrected_text)

    if misspelled:
        result_label.config(text=f"Corrected Sentence: {corrected_sentence}", fg="blue")
    else:
        result_label.config(text="No spelling issues found.", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Spelling Checker")

# User Input
instructions_label = tk.Label(root, text="Enter text to check for spelling issues:", font=("Arial", 14))
instructions_label.pack(pady=10)

user_input = tk.Entry(root, font=("Arial", 14), width=60)
user_input.pack(pady=10)

# Check Button
check_button = tk.Button(root, text="Check Text", font=("Arial", 14), command=check_text)
check_button.pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=600, justify="left")
result_label.pack(pady=10)

# Run the App
root.mainloop()
