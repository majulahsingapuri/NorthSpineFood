import tkinter as tk
import constants

class SubMenu(tk.Frame):

    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

        # Setting title of the SubMenu
        sub_title_label = tk.Label(self, text = "Sub Menu", font = constants.LARGE_FONT)
        sub_title_label.place(relx = 0.2, rely = 0, relheight = 0.05, relwidth = 0.6)