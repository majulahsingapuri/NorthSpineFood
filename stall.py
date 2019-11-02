"""
    stall.py
    North Spine Food
    
    Created by Bhargav Singapuri, Jethro Prahara, Isabela Angus on 170919
    Copyright © 2019 Bhargav Singapuri, Jethro Prahara, Isabela Angus. All rights reserved.
"""

from menu_item import Item
import time
from datetime import datetime
from dateutil.parser import parse

class Stall:
    def __init__(self, stall_name, menu = [Item("Item", 0.00)], waiting_time_factor = 1.4, opening_time = "08:00", closing_time = "18:00", days_available = [0,1,2,3,4,5,6]):
        self.stall_name = stall_name
        self.menu = menu
        self.waiting_time_factor = waiting_time_factor
        self.opening_time = parse(opening_time).time()
        self.closing_time = parse(closing_time).time()
        self.days_available = days_available

    def opening_hours(self):
        return "The opening hours are\n {0} to {1}".format(self.opening_time.strftime("%H:%M"), self.closing_time.strftime("%H:%M"))
        
    def show_price(self, index):
        return "Item: {0:.<30} Price: {1:3.2f}".format(self.menu[index].item_name, self.menu[index].item_cost)
            
    def is_open(self, check_time = datetime.now().time(), check_day = datetime.now().day):

        if isinstance(check_time, str):
            check_time = parse(check_time).time()

        if check_day in self.days_available:
            if self.opening_time <= check_time <= self.closing_time:
                return True
            else:
                return False
        else:
            return False
