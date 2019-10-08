"""
    FoodCourtApp.py
    North Spine Food
    
    Created by Bhargav Singapuri, Jethro Prahara, Isabella Angus on 170919
    Copyright © 2019 Bhargav Singapuri, Jethro Prahara, Isabella Angus. All rights reserved.
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
        self.container = tk.Frame(self, width = constants.START_WIDTH, height = constants.START_HEIGHT)
        self.container.pack(expand = True, fill = "both")

        # Creating an empty dictionary to hold the frames
        self.frames = {}

        # Loading pages into memory
        for F in (MainMenu, SelectStall, AboutUs):
            frame = F(self.container, self)
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
        option_two_button = tk.Button(buttons_frame, text = "About Us", font = constants.MEDIUM_FONT, command = lambda : self.option_two_button_pressed())
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
        stall_buttons_frame.grid_columnconfigure(0, weight = 1)
        stall_buttons_frame.grid_columnconfigure(1, weight = 1)
        stall_buttons_frame.grid_rowconfigure(0, weight = 1)
        stall_buttons_frame.grid_rowconfigure(1, weight = 1)
        stall_buttons_frame.grid_rowconfigure(2, weight = 1)


        # Stall Buttons
        counter = 0
        stall_buttons = []
        for index, stall in enumerate(directory):
            stall_button = tk.Button(stall_buttons_frame, text = stall.stall_name, command = lambda stall = stall : self.stall_button_pressed(stall))
            stall_buttons.append(stall_button)
            if index % 2 == 0:
                stall_button.grid(column = 0, row = counter, sticky = "NSEW", padx = 5, pady = 5)
            else:
                stall_button.grid(column = 1, row = counter, sticky = "NSEW", padx = 5, pady = 5)
                counter += 1


    def back_button_pressed(self):
        app.show_frame(MainMenu)

    def stall_button_pressed(self, stall):
        frame = StallInfo(app.container, app, chosen_stall = stall)
        app.frames[StallInfo] = frame
        frame.place(relheight = 1, relwidth = 1)
        app.show_frame(StallInfo)

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

class StallInfo(tk.Frame):

    def __init__(self, parent, controller, **kw):

        chosen_stall = kw["chosen_stall"]
        kw.pop("chosen_stall")

        tk.Frame.__init__(self, parent, **kw)
        
        # About Us Title
        main_title_label = tk.Label(self, text = chosen_stall.stall_name, font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Back Button
        back_button = tk.Button(self, text = "Back", command = lambda: self.back_button_pressed())
        back_button.place(relx = 0.0125, rely = 0.0625, height = 30, width = 50)

        # Open/Closed Label
        open_closed_label = tk.Label(self, text = "Open!" if chosen_stall.is_open() else "Closed!", font = constants.MEDIUM_FONT)
        open_closed_label.place(relx = 0.25, rely = 0.1875, relheight = 0.0625, relwidth = 0.5)

        # Wait Calculation Frame
        wait_calculation_frame = tk.Frame(self)
        wait_calculation_frame.place(relx = 0.125, rely = 0.3125, relheight = 0.4, relwidth = 0.75)

        # Wait Calculation Entry
        wait_calculation_entry = tk.Entry(wait_calculation_frame, font = constants.SMALL_FONT, state = "normal" if chosen_stall.is_open() else "disabled")
        wait_calculation_entry.bind('<Return>', lambda x : self.calculate_button_pressed(wait_calculation_entry.get(), chosen_stall))
        wait_calculation_entry.place(relx = 0, rely = 0, relwidth = 0.75, relheight = 0.25)

        # Wait Calculation Button
        wait_calculation_button = tk.Button(wait_calculation_frame, text = "Calculate!", command = lambda: self.calculate_button_pressed(wait_calculation_entry.get(), chosen_stall), state = "normal" if chosen_stall.is_open() else "disabled")
        wait_calculation_button.place(relx = 0.75, rely = 0, relwidth = 0.25, relheight = 0.25)

        # Wait Calculation Label
        self.wait_calculation_label = tk.Label(wait_calculation_frame, font = constants.MEDIUM_FONT, text = "Please enter the number\n of people in Queue" if chosen_stall.is_open() else "Stall is closed. Please come\n again when it opens!")
        self.wait_calculation_label.place(relx = 0, rely = 0.25, relwidth = 1, relheight = 0.75)

        # Show menu button
        show_menu_button = tk.Button(self, text = "Show Menu", command = lambda: self.show_menu_button_pressed(chosen_stall))
        show_menu_button.place(relx = 0.125, rely = 0.775, relheight = 0.125, relwidth = 0.75)

    def back_button_pressed(self):
        app.show_frame(SelectStall)

    def calculate_button_pressed(self, entry_text, chosen_stall):
        try:
            num_people_in_queue = float(entry_text)
            self.wait_calculation_label["text"] = str(round(num_people_in_queue, 0) * chosen_stall.waiting_time_factor) + " Minutes to front of Queue!"
        except:
            self.wait_calculation_label["text"] = "Please enter a valid Number!"

    def show_menu_button_pressed(self, stall):
        frame = MenuList(app.container, app, chosen_stall = stall)
        app.frames[MenuList] = frame
        frame.place(relheight = 1, relwidth = 1)
        app.show_frame(MenuList)

class MenuList(tk.Frame):

    def __init__(self, parent, controller, **kw):

        chosen_stall = kw["chosen_stall"]
        kw.pop("chosen_stall")

        tk.Frame.__init__(self, parent, **kw)

        # About Us Title
        main_title_label = tk.Label(self, text = chosen_stall.stall_name, font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Back Button
        back_button = tk.Button(self, text = "Back", command = lambda: self.back_button_pressed())
        back_button.place(relx = 0.0125, rely = 0.0625, height = 30, width = 50)

        # Listbox
        menu_listbox = tk.Listbox(self, font = constants.TERMINAL_FONT)
        for index, _ in enumerate(chosen_stall.menu):
            menu_listbox.insert("end", chosen_stall.show_price(index))
        menu_listbox.place(relx = 0.125, rely = 0.2, relheight = 0.7, relwidth = 0.75)
    
    def back_button_pressed(self):
        app.show_frame(StallInfo)
        

# Running the app loop
app = FoodCourtApp()
app.minsize(constants.MIN_HEIGHT, constants.MIN_WIDTH)
app.mainloop()
