"""
    menu_item.py
    North Spine Food
    
    Created by Bhargav Singapuri, Jethro Prahara, Isabela Angus on 170919
    Copyright © 2019 Bhargav Singapuri, Jethro Prahara, Isabela Angus. All rights reserved.
"""

import time
from datetime import datetime
from dateutil.parser import parse

class Item:
    def __init__(self, item_name = "", item_cost = 0.00, available_from_time = "08:00", available_to_time = "18:00", days_available = [0,1,2,3,4,5,6]):
        self.item_name = item_name
        self.item_cost = item_cost
        self.available_from_time = parse(available_from_time).time()
        self.available_to_time = parse(available_to_time).time()
        self.days_available = days_available

    def is_available(self, check_time = datetime.now().time(), check_day = datetime.now().weekday()):

        if isinstance(check_time, str):
            check_time = parse(check_time).time()

        if check_day in self.days_available:
            if self.available_from_time <= check_time <= self.available_to_time:
                return True
            else:
                return False
        else:
            return False
