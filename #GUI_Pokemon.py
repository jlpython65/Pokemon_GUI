#GUI_Pokemon
from email.mime import image
import imp
import tkinter as tk
from PIL import ImageTk, Image  


#!/usr/bin/python3
import tkinter as tk


class TestApp:
    def __init__(self, master=None):
        # build ui
        self.frame2 = tk.Frame(master)
        self.labelframe1 = tk.LabelFrame(self.frame2)
        self.pokemon = tk.Label(self.labelframe1)
        self.img_Milotic = tk.PhotoImage(file=r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5\Milotic.png")
        self.pokemon.configure(
            font="TkDefaultFont", height=196, image=self.img_Milotic, justify="left"
        )
        self.pokemon.configure(
            relief="flat", state="normal", takefocus=True, text="label1"
        )
        self.pokemon.configure(width=196)
        self.pokemon.pack(side="top")
        self.labelframe1.configure(
            cursor="arrow", height=196, takefocus=False, text="labelframe1"
        )
        self.labelframe1.configure(width=196)
        self.labelframe1.pack(side="top")
        self.frame3 = tk.Frame(self.frame2, container="true")
        self.frame3.configure(cursor="based_arrow_up", height=200, width=500)
        self.frame3.pack(side="top")
        self.button1 = tk.Button(self.frame2)

        catch_icon = tk.PhotoImage(r'C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\GUI\poke_ball.png')

        self.button1.configure(
            anchor="n", borderwidth=25, compound="top", cursor="arrow"
        )
        self.button1.configure(
            default="normal", font="TkTextFont", justify="center", overrelief="sunken"
        )
        self.button1.configure(
            relief="raised", state="active", takefocus=False, text="CATCH", image= catch_icon
        )
        self.frame2.configure(height=200, width=200)
        self.frame2.pack(side="top")

        # Main widget
        self.mainwindow = self.frame2

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TestApp(root)
    app.run()
    print("hello1")

