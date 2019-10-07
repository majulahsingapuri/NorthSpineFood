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
        for F in (MainMenu, SelectStall, AboutUs):
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

    # Parent is the previous frame in the hierarchy, controller is the reference to the app instance
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        # Main Menu Title
        main_title_label = tk.Label(self, text = "Main Menu", font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.place(relx = 0.125, rely = 0.375, relwidth = 0.75, relheight = 0.5)

        # Select Stall Button
        select_stall_button = tk.Button(buttons_frame, text = "Select Stall", font = constants.MEDIUM_FONT, command = lambda : self.select_stall_button_pressed())
        select_stall_button.place(relx = 0.125, rely = 0.125, relheight = 0.25, relwidth = 0.75)

        # Option 2 Button
        option_two_button = tk.Button(buttons_frame, text = "About Us :)", font = constants.MEDIUM_FONT, command = lambda : self.option_two_button_pressed())
        option_two_button.place(relx = 0.125, rely = 0.625, relheight = 0.25, relwidth = 0.75)
    
    def select_stall_button_pressed(self):
        # Changing view to SelectStall
        app.show_frame(SelectStall)

    def option_two_button_pressed(self):
        # Changing view to About Us
        app.show_frame(AboutUs)

class SelectStall(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        # Setting title of the SelectStall
        sub_title_label = tk.Label(self, text = "Select Stall", font = constants.LARGE_FONT)
        sub_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Back Button
        back_button = tk.Button(self, text = "Back", command = lambda: self.back_button_pressed())
        back_button.place(relx = 0.0125, rely = 0.0625, height = 30, width = 50)

        # Frame to hold all Stall Buttons
        stall_buttons_frame = tk.Frame(self)
        stall_buttons_frame.place(relx = 0.125, rely = 0.375, relwidth = 0.75, relheight = 0.5)

        # Stall Buttons
        counter = 0
        for index, stall in enumerate(directory):
            stall_button = tk.Button(stall_buttons_frame, text = stall.stall_name, command = lambda : self.stall_button_pressed(stall))
            if index % 2 == 1:
                stall_button.grid(column = 0, row = counter)
            else:
                stall_button.grid(column = 1, row = counter)
                counter += 1


    def back_button_pressed(self):
        app.show_frame(MainMenu)

    def stall_button_pressed(self, stall):
        print("Chose stall " + stall.stall_name)

class AboutUs(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        # About Us Title
        main_title_label = tk.Label(self, text = "About Us", font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Back Button
        back_button = tk.Button(self, text = "Back", command = lambda: self.back_button_pressed())
        back_button.place(relx = 0.0125, rely = 0.0625, height = 30, width = 50)

    def back_button_pressed(self):
        app.show_frame(MainMenu)

# Running the app loop
app = FoodCourtApp()
app.minsize(200,200)
app.mainloop()
