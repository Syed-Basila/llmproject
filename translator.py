import tkinter as tk
from googletrans import Translator

def translate_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text:
        try:
            translator = Translator()
            translation = translator.translate(input_text, src='en', dest='ta')
            result_label.config(text=f"Translated Text (Tamil): {translation.text}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Please enter text to translate.")

# Create GUI
root = tk.Tk()
root.title("English to Tamil Translator")

# Text input
tk.Label(root, text="Enter Text in English:").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Translate button
translate_button = tk.Button(root, text="Translate to Tamil", command=translate_text)
translate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run GUI
root.mainloop()












