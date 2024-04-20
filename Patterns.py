import tkinter as tk
import random

def draw_pattern(canvas):
    canvas.delete("all")  # Clear the canvas
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for i in range(50):  # Draw 50 random rectangles
        x0 = random.randint(0, 150)
        y0 = random.randint(0, 150)
        x1 = x0 + random.randint(50, 100)
        y1 = y0 + random.randint(50, 100)
        color = random.choice(colors)
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

app = tk.Tk()
app.title("Pattern Generator")

canvas = tk.Canvas(app, width=200, height=200)
canvas.pack()

btn_draw = tk.Button(app, text="Generate Pattern", command=lambda: draw_pattern(canvas))
btn_draw.pack()

app.mainloop()
