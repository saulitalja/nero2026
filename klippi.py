import tkinter as tk
import random

MESSAGES = [
    "Hei! Tarvitsetko apua?",
    "Ime munaa!",
    "Näyttää siltä, että kirjoitat koodia!",
    "Haluatko vinkkejä Pythonista?",
    "Muista tallentaa työsi 💾",
    "Voinko auttaa jossain?"
]

class ClippyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clippy 2.0")

        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # "Clippy" yksinkertaisena silmukkana (ympyrä + silmät)
        self.body = self.canvas.create_oval(120, 120, 180, 200, fill="yellow", outline="black")
        self.eye1 = self.canvas.create_oval(135, 140, 145, 150, fill="black")
        self.eye2 = self.canvas.create_oval(155, 140, 165, 150, fill="black")

        self.text = self.canvas.create_text(150, 260, text="", font=("Arial", 10))

        self.dx = 3
        self.dy = 2

        self.animate()
        self.change_message()

    def animate(self):
        self.canvas.move(self.body, self.dx, self.dy)
        self.canvas.move(self.eye1, self.dx, self.dy)
        self.canvas.move(self.eye2, self.dx, self.dy)

        pos = self.canvas.coords(self.body)

        # bounce
        if pos[0] <= 0 or pos[2] >= 300:
            self.dx *= -1
        if pos[1] <= 0 or pos[3] >= 300:
            self.dy *= -1

        self.root.after(30, self.animate)

    def change_message(self):
        msg = random.choice(MESSAGES)
        self.canvas.itemconfig(self.text, text=msg)
        self.root.after(2000, self.change_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClippyApp(root)
    root.mainloop()