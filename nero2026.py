import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random

# --- Pöllö ---
OWL_UP = """
 ,_,
(0,0)
/| |\\
  |
"""

OWL_DOWN = """
 ,_,
(0,0)
 \\|/
  |
"""

kysymykset = [
    {
        "kysymys": "Mikä ei ole tunnettu protokolla?",
        "vaihtoehdot": ["TCP", "UDP", "IP", "OP"],
        "oikea": "OP"
    },
    {
        "kysymys": "Kuinka monta bittiä on tavussa?",
        "vaihtoehdot": ["4", "8", "16", "32"],
        "oikea": "8"
    }
]

random.shuffle(kysymykset)

idx = 0
pisteet = 0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
ax.axis("off")

text_obj = ax.text(0.5, 0.6, "", ha="center", va="center", fontsize=14)

result_obj = ax.text(0.5, 0.1, "", ha="center", va="center", fontsize=12)

buttons = []

def show_question():
    q = kysymykset[idx]
    text = "🦉 " + q["kysymys"] + "\n\n"
    for i, v in enumerate(q["vaihtoehdot"]):
        text += f"{i+1}) {v}\n"
    text_obj.set_text(text)
    result_obj.set_text("")
    fig.canvas.draw()

def animate_owl(correct):
    if correct:
        for _ in range(3):
            text_obj.set_text(OWL_UP)
            fig.canvas.draw()
            plt.pause(0.15)
            text_obj.set_text(OWL_DOWN)
            fig.canvas.draw()
            plt.pause(0.15)

def check_answer(label):
    global idx, pisteet

    if idx >= len(kysymykset):
        return

    q = kysymykset[idx]

    if label == q["oikea"]:
        pisteet += 1
        result_obj.set_text("🦉 Oikein!")
        animate_owl(True)
    else:
        result_obj.set_text(f"🦉 Väärin! Oikea: {q['oikea']}")

    idx += 1

    if idx < len(kysymykset):
        show_question()
    else:
        text_obj.set_text(f"🦉 Peli ohi!\nPisteet: {pisteet}/{len(kysymykset)}")
        for b in buttons:
            b.ax.set_visible(False)
        fig.canvas.draw()

# --- napit ---
labels = ["TCP", "UDP", "IP", "OP", "4", "8", "16", "32"]

x_pos = [0.05, 0.25, 0.45, 0.65, 0.05, 0.25, 0.45, 0.65]
y_pos = [0.05]*4 + [0.15]*4

for i, label in enumerate(labels):
    ax_button = plt.axes([x_pos[i], y_pos[i], 0.18, 0.08])
    btn = Button(ax_button, label)
    btn.on_clicked(lambda event, l=label: check_answer(l))
    buttons.append(btn)

show_question()
plt.show()