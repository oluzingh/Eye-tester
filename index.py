from tkinter import *
import random

class EyeTester:
    def __init__(self, master):
        self.master = master
        master.title("Eye Tester")
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Create a list of letters to display
        self.letters = ["E", "F", "D", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # Initialize the font size and letter to display
        self.font_size = 100
        self.letter = random.choice(self.letters)

        # Display the first letter
        self.draw_letter()

        # Bind the mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_letter(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Generate a random color for the letter
        color = "#%06x" % random.randint(0, 0xFFFFFF)

        # Set the font size and color
        font = ("Arial", self.font_size)
        self.canvas.create_text(150, 150, text=self.letter, font=font, fill=color)

    def on_click(self, event):
        # Reduce the font size
        self.font_size -= 10

        # If the font size is less than 20, display a new letter and reset the font size
        if self.font_size < 20:
            self.font_size = 100
            self.letter = random.choice(self.letters)
        else:
            # Otherwise, redraw the letter with the new font size
            self.draw_letter()

# Create the window and start the EyeTester
root = Tk()
my_eye_tester = EyeTester(root)
root.mainloop()