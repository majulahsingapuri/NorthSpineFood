"""
    stall.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
"""

from menu_item import Item
import time
from datetime import datetime
from dateutil.parser import parse

class Stall:
    def __init__(self, stall_name, menu = [Item("Item", 0.00)], waiting_time_factor = 1.4, opening_time = "08:00", closing_time = "18:00"):
        self.stall_name = stall_name
        self.menu = menu
        self.waiting_time_factor = waiting_time_factor
        
        """
            Need to do some processing here and store the value as time rather than a string
        """
        self.opening_time = parse(opening_time).time()
        self.closing_time = parse(closing_time).time()

    def opening_hours(self):
        print("The opening hours are", self.opening_time.strftime("%H:%M") , "to", self.closing_time.strftime("%H:%M"))
        
    def show_price(self):
        print("The items in this stall are: ", end = '\n\n\n')
        for item in self.menu:
            print("Item: {0:15}{1:10}Price: {2:3.2f}".format(item.item_name, " ",item.item_cost))

            """
                Finalise formatting for this
            """
            
    def is_open(self, check_time = datetime.now().time()):

        if isinstance(check_time, str):
            check_time = parse(check_time).time()

        if self.opening_time <= check_time <= self.closing_time:
            return True
        else:
            return False
