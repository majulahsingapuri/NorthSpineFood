"""
    FoodCourtApp.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
"""

from stall import Stall
from menu_item import Item
from data import directory
import tkinter as tk

HEIGHT = 400
WIDTH = 400
LARGE_FONT = ("Verdana", 12)

class FoodCourtApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # Basic initialisation of the app
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Food Court App")
        
        # Setting the Main Frame that will hold all other widgets
        container = tk.Frame(self, width = WIDTH, height = HEIGHT)
        container.pack(expand = True, fill = "both")

        # Creating an empty dictionary to hold the frames
        self.frames = {}

        # Loading pages into memory
        for F in (MainMenu, SubMenu):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relheight = 1, relwidth = 1)
        
        # Showing the inital page
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        # Fetching the required frame and bringing it to the top of the view
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        main_title_label = tk.Label(self, text = "Main Menu", font = LARGE_FONT)
        main_title_label.place(relx = 0.2, rely = 0, relheight = 0.05, relwidth = 0.6)

        go_to_sub_menu_button = tk.Button(self, text = "Sub Menu", command = lambda: controller.show_frame(SubMenu))
        go_to_sub_menu_button.place(relheight = 0.6, relwidth = 0.6, rely = 0.2, relx = 0.2)


class SubMenu(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        sub_title_label = tk.Label(self, text = "Sub Menu", font = LARGE_FONT)
        sub_title_label.place(relx = 0.2, rely = 0, relheight = 0.05, relwidth = 0.6)

# Running the app loop
app = FoodCourtApp()
app.mainloop()


"""
    Things to do:
        - Create the User Interface for the whole app
        - Move the individual Classes to their own file
"""
