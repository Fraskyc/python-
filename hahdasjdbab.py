import tkinter as tk

def count_spaces():
    text = input_field.get()

    count = 1
    prev_char = ""
    for char in text:
        if char == " " and prev_char != " ":
            count += 1
        prev_char = char

    output_label.config(text="Number of words: " + str(count))

window = tk.Tk()
window.title("Count words")

input_field = tk.Entry(window)
input_field.pack()

count_button = tk.Button(window, text="Count words", command=count_spaces)
count_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
