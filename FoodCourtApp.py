"""
    FoodCourtApp.py
    North Spine Food
    
    Created by Bhargav Singapuri, Jethro Prahara, Isabela Angus on 170919
    Copyright © 2019 Bhargav Singapuri, Jethro Prahara, Isabela Angus. All rights reserved.
"""

from stall import Stall
from menu_item import Item
from data import directory
from datetime import datetime
from tkcalendar import DateEntry
import time
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
    
    # Changing view to SelectStall
    def select_stall_button_pressed(self):
        app.show_frame(SelectStall)

    # Changing view to About Us
    def option_two_button_pressed(self):
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

        # Configures the 2 Grids for the Stall Buttons
        stall_buttons_frame.grid_columnconfigure(0, weight = 1)
        stall_buttons_frame.grid_columnconfigure(1, weight = 1)

        # Configures rows for Stall Buttons Based on how many Stalls are Present
        count = sum(1 for x in directory if isinstance(x, Stall))
        if count % 2 == 1:
            count += 1
        for index in range(int(count/2)):
            stall_buttons_frame.grid_rowconfigure(index, weight = 1)

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

    # Navigates back to Main Menu
    def back_button_pressed(self):
        app.show_frame(MainMenu)

    # Creates new/overrides old instance of Stall Info and navigates
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

    # Navigates back to Main Menu
    def back_button_pressed(self):
        app.show_frame(MainMenu)

"""
    Things to do:
        - Fill up About Us with something
"""

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
        open_closed_label = tk.Label(self, text = "Open!" if chosen_stall.is_open() else chosen_stall.opening_hours(), font = constants.MEDIUM_FONT)
        open_closed_label.place(relx = 0.25, rely = 0.1875, relheight = 0.0625, relwidth = 0.5)

        # Wait Calculation Frame
        wait_calculation_frame = tk.Frame(self)
        wait_calculation_frame.place(relx = 0.125, rely = 0.3125, relheight = 0.4, relwidth = 0.75)

        # Wait Calculation Entry - Disabled if Stall is closed
        wait_calculation_entry = tk.Entry(wait_calculation_frame, font = constants.SMALL_FONT, state = "normal" if chosen_stall.is_open() else "disabled")
        wait_calculation_entry.bind('<Return>', lambda x : self.calculate_button_pressed(wait_calculation_entry.get(), chosen_stall))
        wait_calculation_entry.place(relx = 0, rely = 0, relwidth = 0.75, relheight = 0.25)

        # Wait Calculation Button - Disabled if Stall is closed
        wait_calculation_button = tk.Button(wait_calculation_frame, text = "Calculate!", command = lambda: self.calculate_button_pressed(wait_calculation_entry.get(), chosen_stall), state = "normal" if chosen_stall.is_open() else "disabled")
        wait_calculation_button.place(relx = 0.75, rely = 0, relwidth = 0.25, relheight = 0.25)

        # Wait Calculation Label - Default message if Stall is closed
        self.wait_calculation_label = tk.Label(wait_calculation_frame, font = constants.MEDIUM_FONT, text = "Please enter the number\n of people in Queue" if chosen_stall.is_open() else "Stall is closed. Please come\n again when it opens!")
        self.wait_calculation_label.place(relx = 0, rely = 0.25, relwidth = 1, relheight = 0.75)

        # Show menu button
        show_menu_button = tk.Button(self, text = "Show Menu", command = lambda: self.show_menu_button_pressed(chosen_stall))
        show_menu_button.place(relx = 0.125, rely = 0.775, relheight = 0.125, relwidth = 0.75)

    # Navigates back to Select Stall
    def back_button_pressed(self):
        app.show_frame(SelectStall)

    # Calculates waiting time based on people in Queue
    def calculate_button_pressed(self, entry_text, chosen_stall):
        try:
            num_people_in_queue = float(entry_text)
            if num_people_in_queue < 0 or num_people_in_queue > 50:
                raise RangeError
            self.wait_calculation_label["text"] = str(round(num_people_in_queue, 0) * chosen_stall.waiting_time_factor) + " Minutes to front of Queue!"
        # Raised when input is not a number
        except ValueError:
            self.wait_calculation_label["text"] = "Please enter a valid Number!"
        # Raised when entered number is out of range
        except RangeError:
            self.wait_calculation_label["text"] = "Value out of Range"

    # Creates a new/overrides old instance of Menu List with the given stall 
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

        # Main Title
        main_title_label = tk.Label(self, text = chosen_stall.stall_name, font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Back Button
        back_button = tk.Button(self, text = "Back", command = lambda: self.back_button_pressed())
        back_button.place(relx = 0.0125, rely = 0.0625, height = 30, width = 50)

        # Listbox
        self.menu_listbox = tk.Listbox(self, font = constants.TERMINAL_FONT)
        self.list_reload_data(chosen_stall)
        self.menu_listbox.place(relx = 0.125, rely = 0.2, relheight = 0.6, relwidth = 0.75)
        app.geometry("500x300")

        # Time Picker Button
        time_picker_button = tk.Button(self, text = "Check menu at specific time", command = lambda: self.time_picker_button_pressed(chosen_stall))
        time_picker_button.place(relx = 0.125, rely = 0.85, relheight = 0.1, relwidth = 0.75)
    
    # Navigates back to Stall Info page and closes any Time Picker pages if open
    def back_button_pressed(self):
        app.show_frame(StallInfo)
        TimePicker.destroy(self)

    # Opens a new Window with a Time Picker and sets its dimensions
    def time_picker_button_pressed(self, chosen_stall):
        time_picker = TimePicker(self, chosen_stall = chosen_stall)
        time_picker.title("Time Picker")
        time_picker.minsize(constants.MIN_HEIGHT, constants.MIN_WIDTH)

    # Reloads data in Menu List based on either system time or user entered time
    def list_reload_data(self, chosen_stall, check_time = "", check_day = datetime.today().day):
        self.menu_listbox.delete(0, "end")
        if check_time == "":
            for index, item in enumerate(chosen_stall.menu):
                if item.is_available():
                    self.menu_listbox.insert("end", chosen_stall.show_price(index))
        else:
            for index, item in enumerate(chosen_stall.menu):
                if item.is_available(check_time, check_day):
                    self.menu_listbox.insert("end", chosen_stall.show_price(index))
        
class TimePicker(tk.Toplevel):

    def __init__(self, parent, **kw):

        chosen_stall = kw["chosen_stall"]
        kw.pop("chosen_stall")

        tk.Toplevel.__init__(self, parent, **kw)

        # Main Title
        main_title_label = tk.Label(self, text = "Select Timing", font = constants.MEDIUM_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Spinbox Frame
        spinbox_frame = tk.Frame(self)
        spinbox_frame.place(relx = 0.125, rely = 0.25, relheight = 0.25, relwidth = 0.75)

        # Spinboxes
        hour = tk.IntVar(value = datetime.now().time().hour)
        self.hour_spinbox = tk.Spinbox(spinbox_frame, from_ = 00, to = 23, increment = 1, textvariable = hour, format = "%02.0f", state = "readonly")
        self.hour_spinbox.place(relx = 0, rely = 0.25, relheight = 1, relwidth = 0.3)
        minute = tk.IntVar(value = (((datetime.now().time().minute // 10) * 10)))
        self.minute_spinbox = tk.Spinbox(spinbox_frame, from_ = 00, to = 50, increment = 10, textvariable = minute, format = "%02.0f", state = "readonly")
        self.minute_spinbox.place(relx = 0.3, rely = 0.25, relheight = 1, relwidth = 0.3)
        self.date_entry = DateEntry(spinbox_frame, state = "normal", firstweekday = "monday", mindate = datetime.today().date(), showweeknumbers = False, showothermonthdays = False, locale = "en_SG", date_pattern = "dd-mm-yyyy")
        self.date_entry.place(relx = 0.6, rely = 0.25, relheight = 1, relwidth = 0.4)

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.place(relx = 0.125, rely = 0.625, relheight = 0.25, relwidth = 0.75)

        # Current Time Button
        current_time_button = tk.Button(buttons_frame, text = "Now", command = lambda: self.current_time_button_pressed())
        current_time_button.place(relx = 0.125, rely = 0.125, relheight = 0.25, relwidth = 0.75)

        # Submit button
        submit_button = tk.Button(buttons_frame, text = "Submit", command = lambda: self.submit_button_pressed(self.hour_spinbox.get(), self.minute_spinbox.get(), self.date_entry.get_date(), parent, chosen_stall))
        submit_button.place(relx = 0.125, rely = 0.5, relheight = 0.25, relwidth = 0.75)

    # Takes entered Time from Spinboxes and updates the Menu List
    def submit_button_pressed(self, hour_time, minute_time, on_day, parent, chosen_stall):
        hour_time = int(hour_time)
        minute_time = int(minute_time)
        time = str(hour_time).format("%02.0f") + ":" + str(minute_time).format("%02.0f")
        parent.list_reload_data(chosen_stall, time, on_day.weekday())
        self.destroy()

    # Resets Hour and Minute in Spinbox to Current Time
    def current_time_button_pressed(self):
        hour = tk.IntVar(value = datetime.now().time().hour)
        minute = tk.IntVar(value = (((datetime.now().time().minute // 10) * 10)))
        self.hour_spinbox["textvariable"] = hour
        self.minute_spinbox["textvariable"] = minute
        self.date_entry.set_date(datetime.now().date())

class RangeError(Exception):
    pass

# Running the app loop
app = FoodCourtApp()
app.minsize(constants.MIN_HEIGHT, constants.MIN_WIDTH)
app.mainloop()
