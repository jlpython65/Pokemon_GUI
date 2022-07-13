#!/usr/bin/python3
import os, random
import tkinter as tk
import tkinter.ttk as ttk

image =random.choice(os.listdir(r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5"))
image_name = image.replace(".png","" )

class StartApp:
    def __init__(self, master=None):
        # build ui
        self.frame2 = tk.Frame(master)
        self.frame1 = ttk.Frame(self.frame2)
        self.pokemon = tk.Label(self.frame1)
        self.img_POKEMON = tk.PhotoImage(file=fr"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5\{image}")
        self.pokemon.configure(
            anchor="center", bitmap="error", font="TkTextFont", height=196
        )
        self.pokemon.configure(
            image=self.img_POKEMON, justify="center", relief="raised", state="normal"
        )
        self.pokemon.configure(takefocus=False, text="label1", width=196)
        self.pokemon.pack()
        self.frame1.configure(height=500, width=500)
        self.frame1.grid(column=0, row=0, sticky="n")
        self.frame3 = ttk.Frame(self.frame2)
        self.button1 = tk.Button(self.frame3)
        self.button1.configure(
            borderwidth=10, default="normal", font="TkDefaultFont", justify="right"
        )
        self.button1.configure(state="normal", text="CATCH")
        self.button1.pack(side="left")
        self.label3 = ttk.Label(self.frame3)
        self.img_pokeball1 = tk.PhotoImage(file=r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\GUI\pokeball (1).png")
        self.label3.configure(
            compound="center",
            font="{Arial Narrow} 12 {bold}",
            foreground="#fb5846",
            image=self.img_pokeball1,
        )
        self.label3.pack(expand="true", padx=20, side="top")
        self.label4 = ttk.Label(self.frame3)
        self.label4.configure(text="10x")
        self.label4.pack(side="top")
        self.frame3.configure(cursor="arrow", height=100, width=200)
        self.frame3.grid(column=0, row=2)
        self.frame2.configure(height=300, relief="flat", takefocus=False, width=300)
        self.frame2.grid(column=0, row=0)
        self.frame7 = ttk.Frame(self.frame2)
        self.frame7.configure(width=300)
        self.frame7.grid()
        self.frame2.configure(cursor="arrow", height=300, relief="flat", takefocus=True)


        # Main widget
        self.mainwindow = self.frame2

    def run(self):
        self.mainwindow.mainloop()


class CatchApp:
    def __init__(self, master=None):
        # build ui
        self.frame2 = tk.Frame(master)
        self.frame1 = ttk.Frame(self.frame2)
        self.pokemon = tk.Label(self.frame1)
        self.img_Absol = tk.PhotoImage(file=fr"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5\{image}")
        self.pokemon.configure(
            anchor="center", font="TkDefaultFont", height=196, image=self.img_Absol
        )
        self.pokemon.configure(
            justify="center", relief="raised", state="normal", takefocus=False
        )
        self.pokemon.configure(text="label1", width=196)
        self.pokemon.pack()
        self.frame1.configure(height=500, takefocus=False, width=500)
        self.frame1.grid(column=0, row=0, sticky="n")
        self.frame3 = ttk.Frame(self.frame2)
        self.label1 = ttk.Label(self.frame3)
        self.label1.configure(
            takefocus=False,
            text=f"{image_name} has been caught! Would you like to give a nickname?",
        )
        self.label1.pack(side="top")
        self.entry2 = ttk.Entry(self.frame3)
        self.entry2.pack(side="top")
        self.frame3.configure(cursor="arrow", height=100, width=200)
        self.frame3.grid(column=0, row=2)

        self.frame2.configure(height=300, relief="flat", takefocus=False, width=300)
        self.frame2.grid(column=0, row=0)

        # Main widget
        self.mainwindow = self.frame2

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StartApp(root)
    app.button1.bind("<Button>", 
        lambda change_root, delete_start: CatchApp(root),app.frame1. destroy()) #picture gets deleted here so attach destroy to a button command 
    app.run()
    
