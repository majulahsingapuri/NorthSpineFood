"""
    FoodCourtApp.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
"""

from stall import Stall
from menu_item import Item
from data import directory
from main_menu import MainMenu
from sub_menu import SubMenu
import tkinter as tk
import constants

class FoodCourtApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # Basic initialisation of the app
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Food Court App")
        
        # Setting the Main Frame that will hold all other widgets
        container = tk.Frame(self, width = constants.WIDTH, height = constants.WIDTH)
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

# Running the app loop
app = FoodCourtApp()
app.mainloop()
