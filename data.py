"""
    data.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
    """


from stall import Stall
from menu_item import Item

noodle_stall = Stall("Noodle Stall", [Item("Wanton Noodle", 4.20), Item("Fishball Noodle", 6.90)], 1.6, "08:00", "18:00")

directory = [noodle_stall]
"""
    Things to do:
        Hard code all the starting data for the app
            - all the stalls and the items that they sell
        Create an Array of all the stalls and call it directory
"""
