import tkinter as tk
import math
import random
from tkinter import ttk

class MandalaApp:
    def __init__(self, master):
        self.master = master
        master.title("Dynamic Mandala Generator")

        self.canvas = tk.Canvas(master, width=640, height=480, bg='black')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.running = False
        self.speed = 100
        self.shape = 10
        self.intensity = 10
        self.thickness = 2

        # Controls frame
        controls_frame = ttk.Frame(master)
        controls_frame.pack(fill=tk.X, expand=False)

        # Speed slider
        ttk.Label(controls_frame, text="Speed").pack(side=tk.LEFT)
        self.speed_slider = ttk.Scale(controls_frame, from_=1, to=1500, orient="horizontal", command=self.update_speed)
        self.speed_slider.set(self.speed)
        self.speed_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Shape slider
        ttk.Label(controls_frame, text="Shape").pack(side=tk.LEFT)
        self.shape_slider = ttk.Scale(controls_frame, from_=3, to=50, orient="horizontal", command=self.update_shape)
        self.shape_slider.set(self.shape)
        self.shape_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Intensity slider
        ttk.Label(controls_frame, text="Intensity").pack(side=tk.LEFT)
        self.intensity_slider = ttk.Scale(controls_frame, from_=5, to=50, orient="horizontal", command=self.update_intensity)
        self.intensity_slider.set(self.intensity)
        self.intensity_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Thickness slider
        ttk.Label(controls_frame, text="Thickness").pack(side=tk.LEFT)
        self.thickness_slider = ttk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=self.update_thickness)
        self.thickness_slider.set(self.thickness)
        self.thickness_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Start/Stop Button
        self.start_button = ttk.Button(master, text="Start", command=self.toggle)
        self.start_button.pack(fill=tk.X)

        self.update_mandala()

    def toggle(self):
        self.running = not self.running
        self.start_button.config(text="Stop" if self.running else "Start")
        if self.running:
            self.update_mandala()

    def update_speed(self, event):
        self.speed = int(self.speed_slider.get())

    def update_shape(self, event):
        self.shape = int(self.shape_slider.get())

    def update_intensity(self, event):
        self.intensity = int(self.intensity_slider.get())

    def update_thickness(self, event):
        self.thickness = int(self.thickness_slider.get())

    def update_mandala(self):
        if self.running:
            self.canvas.delete("all")
            angle_step = 2 * math.pi / self.shape
            max_radius = min(320, 240)
            colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'white']

            for _ in range(self.intensity):
                r = random.randint(20, max_radius)
                color = random.choice(colors)
                for i in range(self.shape):
                    x = 320 + int(r * math.cos(i * angle_step))
                    y = 240 + int(r * math.sin(i * angle_step))
                    self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=color, width=self.thickness)

            self.master.after(self.speed, self.update_mandala)

if __name__ == "__main__":
    root = tk.Tk()
    app = MandalaApp(root)
    root.mainloop()
