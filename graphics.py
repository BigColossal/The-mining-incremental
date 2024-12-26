import tkinter as tk

class Window:

    def __init__(self, width, height, background_color):
        self._root = tk.Tk()
        self._background_color = background_color
        self._root.title("The Mining Incremental")
        self._root.resizable(True, True)
        self._canvas = tk.Canvas(self._root, bg=self._background_color, height=height, width=width)
        self._canvas.pack(fill=tk.BOTH, expand=1)
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._root.after(100, self.main_menu)

    def run(self):
        self._root.mainloop()

    def close(self):
        self._root.destroy()

    
    def clear_screen(self):
        self._canvas.delete("all")


    def text_creation(self, pos_x, pos_y, text, size):
        return self._canvas.create_text(pos_x, pos_y, text=text, font=("Arial", size), fill="black")

    def rectangle_creation(self, pos_x, pos_y, size_x, size_y):
        return self._canvas.create_rectangle(pos_x - size_x // 2, pos_y - size_y // 2, pos_x + size_x // 2, pos_y + size_y // 2, fill="white")

    def button_creation(self, func, pos_x, pos_y, text, text_size, size_x, size_y):
        # Create the button widget
        button = self.rectangle_creation(pos_x, pos_y, size_x, size_y)
        text = self.text_creation(pos_x, pos_y, text, text_size)
        self._canvas.tag_bind(button, "<Button-1>", func)
        self._canvas.tag_bind(text, "<Button-1>", func)



    def main_menu(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self.text_creation(canvas_width // 2, 100, "The Mining Incremental", 50)
        self.text_creation(150, canvas_height - 50, "Created by Jeremy Perez", 20)
        self.button_creation(self.main_game, canvas_width // 2, 300, "Play", 25, 100, 50)

    def main_game(self, event):
        self.clear_screen()
