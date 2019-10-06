from stall import Stall
from menu_item import Item
from data import directory
from sub_menu import SubMenu
import tkinter as tk
import constants


class MainMenu(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        # Main Menu Title
        main_title_label = tk.Label(self, text = "Main Menu", font = constants.LARGE_FONT)
        main_title_label.place(relx = 0.25, rely = 0.0625, relheight = 0.125, relwidth = 0.5)

        # Buttons Frame
        buttons_frame = tk.Frame(self)
        buttons_frame.place(relx = 0.125, rely = 0.375, relwidth = 0.75, relheight = 0.5)

        # Select Stall Button
        select_stall_button = tk.Button(buttons_frame, text = "Select Stall", font = constants.MEDIUM_FONT, command = lambda : self.select_stall_button_pressed(controller))
        select_stall_button.place(relx = 0.125, rely = 0.125, relheight = 0.25, relwidth = 0.75)

        # Option 2 Button
        option_two_button = tk.Button(buttons_frame, text = "Option 2", font = constants.MEDIUM_FONT, command = lambda : self.option_two_button_pressed())
        option_two_button.place(relx = 0.125, rely = 0.625, relheight = 0.25, relwidth = 0.75)
    
    def select_stall_button_pressed(self, controller):
        # Changing view to SubMenu
        controller.show_frame(SubMenu)

    def option_two_button_pressed(self):
        # Whatever this button does
        print("Option 2 pressed")