#!/usr/bin/python3
import os, random
import tkinter as tk
import tkinter.ttk as ttk

image =random.choice(os.listdir(r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5"))
image_name = image.replace(".png","" )

def API():
    #API_Beeminder
    import time
    from pyminder.pyminder import Pyminder

    pyminder = Pyminder(user='Jason Lee', token='7AwyVncx3rLCwAYjJopP')
    goals = pyminder.get_goals()
    goal = goals[0]
    print(goal)
    
    now = time.time()
    yesterday = time.time() - 77760 # .9 of a day = 77760 sec
    sum_ = goal.get_data_sum(now)
    yesterday_sum = goal.get_data_sum(yesterday)
    sess_done = sum_ - yesterday_sum
    needed = goal.get_needed(now)
    print(sess_done)


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
        self.frame2.pack()
        self.frame7 = ttk.Frame(self.frame2)
        self.frame7.configure(width=300)
        self.frame7.grid()
        self.frame2.configure(cursor="arrow", height=300, relief="flat", takefocus=True)

class CatchApp:
    def __init__(self, master=None):
        # build ui
        self.frame2 = tk.Frame(master)
        self.frame1 = ttk.Frame(self.frame2)
        self.pokemon = tk.Label(self.frame1)
        self.img_Absol = tk.PhotoImage(file=fr"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5\Absol.png")
        self.pokemon.configure(
            anchor="center", bitmap="error", font="TkTextFont", height=196
        )
        self.pokemon.configure(
            image=self.img_Absol, justify="center", relief="raised", state="normal"
        )
        self.pokemon.configure(takefocus=False, text="label1", width=196)
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
        self.frame2.pack()



if __name__ == "__main__":
    API()
    root = tk.Tk()
    app = StartApp(root)
    def start_to_catch():
        app2 = CatchApp(root)
        app2.frame2.pack(fill='both',expand=1)
        app.frame2.forget()
    app.button1.config(command=start_to_catch) 
    root.mainloop()

    
