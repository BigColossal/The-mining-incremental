import tkinter as tk
from mobs import Mobs

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


    def title_creation(self, text, subtitle=False):
        canvas_width = self._canvas.winfo_width()
        if subtitle:
            return self.text_creation(canvas_width // 2, 75, text, 40)
        else:
            return self.text_creation(canvas_width // 2, 100, text, 50)
    
    def back_button_creation(self, previous_screen):
        return self.button_creation(previous_screen, 25, 25, "<-", 30, 50, 50)
    
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
        self.title_creation("The Mining Incremental")
        self.text_creation(150, canvas_height - 50, "Created by Jeremy Perez", 20)
        self.button_creation(self.main_game_screen, canvas_width // 2, 300, "Play", 25, 100, 50)

    def main_game_screen(self, event):
        self.clear_screen()
        self.button_creation(self.mob_fighting_screen, 100, 75, "Fight", 25, 75, 35)
        self.button_creation(self.mining_screen, 100, 150, "Mine", 25, 75, 35)

    def mob_fighting_screen(self, event):
        self.clear_screen()
        self.title_creation("Mob Fighting", True)
        self.back_button_creation(self.main_game_screen)
        count = 0
        mob_health = 4
        for mob in Mobs:
            count += 1
            pos_y = count * 75
            mob_health = round(mob_health ** 1.5)
            mob_level = count ** 2

            
            self.text_creation(100, pos_y, mob, 25)
            self.text_creation(45, pos_y + 25, f"Level {mob_level}", 20)
            self.button_creation(lambda event, mob=mob, mob_health=mob_health: self.mob_tiers_screen(mob, mob_health), 120, pos_y + 25, "Select", 20, 40, 25)

    def mob_tiers_screen(self, mob, mob_health):
        print(mob)
        print(mob_health)
        self.clear_screen()
        self.title_creation(mob, True)
        self.back_button_creation(self.mob_fighting_screen)

        

        self.text_creation(100, 175, f"Inferior {mob}", 25)
        self.text_creation(65, 200, f"Health {mob_health - (mob_health // 4)}", 20)
        self.button_creation(self.mob_fighting_screen, 150, 200, "Kill", 20, 40, 25)

        self.text_creation(100, 350, f"Superior {mob}", 25)
        self.text_creation(65, 375, f"Health {mob_health}", 20)
        self.button_creation(self.mob_fighting_screen, 150, 375, "Kill", 20, 40, 25)

        self.text_creation(100, 525, f"Elite {mob}", 25)
        self.text_creation(65, 550, f"Health {mob_health + (mob_health // 4)}", 20)
        self.button_creation(self.mob_fighting_screen, 150, 550, "Kill", 20, 40, 25)

    def mining_screen(self, event):
        self.clear_screen()
        self.title_creation("Mining", True)
        self.back_button_creation(self.main_game_screen)
        
