"""
    stall.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
"""

from menu_item import Item
#import time

class Stall:
    def __init__(self, stall_name, menu = [Item("Item", 0.00)], waiting_time_factor = 1.4, opening_time = "something", closing_time = "something"):
        self.stall_name = stall_name
        self.menu = menu
        self.waiting_time_factor = waiting_time_factor
        
        """
            Need to do some processing here and store the value as time rather than a string
        """
        self.opening_time = opening_time
        self.closing_time = closing_time

    def opening_hours(self):
        print("The opening hours are ", self.opening_time , " to ", self.closing_time)

        """
            Still needs to be improved with the use of a time class variable 
        """

        """
            Still to add:
                Function to display all items and their prices
                    - takes in self
                    - for loop to iterate through items and print( item name, cost) with formatting
                Function to check if stall is open at specified time
                    - takes in self and current time
                    - returns bool to indicate if open or closed
        """
