from tkinter import*
window = Tk()
window.title("Event Handler")
window.geometry("300x200")   # Bigger window so you can see it

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print("Key pressed:", event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("The button was clicked")

button = Button(text="Click me")
button.pack(pady=20)  # Add some space
button.bind("<Button-1>", handle_click)

window.mainloop()
