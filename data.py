"""
    data.py
    North Spine Food
    
    Created by Bhargav Singapuri on 170919
    Copyright © 2019 Bhargav Singapuri. All rights reserved.
    """


from stall import Stall
from menu_item import Item

noodle_stall = Stall("Noodle Stall", [Item("Mee Hoon Kueh", 3.00), 
									  Item("You Mian", 3.00),
									  Item("Mee Sua", 3.00),
									  Item("Yi Mein", 3.00),
									  Item("Thin Bee Hoon", 3.00),
									  Item("Sichuan Veg Banmian", 3.50),
									  Item("Dumpling Banmian", 3,50),
									  Item("Tom Yum Banmian", 3.50),
									  Item("Spicy & Sour Noodles", 3.50),
									  Item("Zha Jiang Mian", 3.50),
									  Item("Sliced Fish Banmian", 3.80),
									  Item("Sliced Fish Bee Hoon", 3.80),
									  Item("Fried Fish Bee Hoon", 3.80),
									  Item("Fried Fish Soup", 3.80),
									  Item("Sliced Fish Soup", 3.80),
									  Item("Fish Porridge", 3,80),
									  Item("6pcs Fried Dumplings", 3.80),
									  Item("6pcs Steamed Dumplings", 3.30)],
					1.6, "0800", "2000")
mixed_rice_stall = Stall("Mixed Rice Stall", [Item("1 fish 1 meat", 4.00), 
				   							  Item("1 meat 1 veg",2.40), 
				  							  Item("3 veg",2.30), 
				   							  Item("2 meat 2 veg",4.40)],
				   		1.6, "0800", "2000")
salad_stall = Stall("Salad Stall", [Item("Chicken Salad", 3.90), 
									Item("Smoked Salmon Salad", 4.50), 
									Item("Egg Salad", 3.90), 
									Item("Smoked Duck Salad", 4.50),
									Item("Tofu Salad", 3.90),
									Item("Gyudon Beef Bowl", 4.90),
									Item("Vegan Bowl", 3.90),
									Item("Smoked Salmon Bowl", 4.90),
									Item("Chicken Bowl", 3.90)
									Item("Smoked Duck Bowl", 4.90)],
					1.6, "0800", "2000")
western_stall = Stall("Western Stall", [Item("Spaghetti with Sausage", 4.80),
										Item("spaghetti with Popcorn", 4.80),
										Item("Spaghetti with Beef Steak", 6.30),
										Item("Spaghetti with Fish and Chips", 4.80),
										Item("Spaghetti with Chicken Chop", 4.80),
										Item("Spaghetti with Chicken Cutlet", 4.80),
										Item("Sausage Rice", 4.80),
										Item("Chicken Popcorn Rice", 4.80),
										Item("Fish and Chips Rice", 4.80),
										Item("Chicken Cutlet Rice", 4.80),
										Item("Beef Steak Rice", 6.30),
										Item("American Breakfast Set", 4.30)],
					 1.6, "0800", "2000")
indian_stall = Stall("Indian Stall", [Item("Plain prata (min 2pcs)", 0.80),
									  Item("Prata Plaster", 1.30),
									  Item("Onion Prata", 1.30),
									  Item("Egg Prata", 1.30),
									  Item("Cheese Prata", 1.70),
									  Item("Egg Onion Prata", 2.00),
									  Item("Cheese Egg Prata", 2.50),
									  Item("Butter Prata", 1.70),
									  Item("Banana Prata", 2.00),
									  Item("Masala Prata", 2.00),
									  Item("Strawberry Prata", 2.00),
									  Item("Chocolate Prata", 2.00),
									  Item("Hotdog Prata", 2.00),
									  Item("Egg Mushroom Prata", 2.50),
									  Item("Mushroom Cheese Prata", 2.50),
									  Item("Hotdog Cheese Prata", 2.50),
									  Item("Mutton Murtabak", 5.00),
									  Item("Chicken Murtabak", 5.00),
									  Item("Sardine Murtabak", 5.00),
									  Item("Nasi Goreng", 3.00),
									  Item("Mee Goreng", 3.00),
									  Item("Kway Teow", 3.00),
									  Item("Bee Hoon", 3.00),
									  Item("Maggi", 3.00),
									  Item("Cheese Roti John", 3.00),
									  Item("Chicken Roti John", 4.00),
									  Item("Mutton Roti John", 4.00),
									  Item("Mutton Briyani", 4.50),
									  Item("Chicken Briyani", 4.50),
									  Item("Fish Briyani", 4.50)],
					1.6, "0800", "2000")
malay_stall = Stall("Malay Stall", [Item("Chicken Nasi Padang", 2.80),
									Item("Beef Rendang", 2.50),
									Item("Assam Fish", 2.00),
									Item("Sambal Goreng", 1.00),
									Item("Vegetable", 0.80),
									Item("3pcs Fishball", 1.20),
									Item("3pcs Ngoh Hiang", 1.20),
									Item("Fish Cake", 0.80),
									Item("Plain Rice", 0.50),
									Item("Noodles", 1.00),
									Item("Bbq Chicken", 4.00),
									Item("Fish Fillet", 4.00),
									Item("Fish Fillet Meal", 5.20),
									Item("Ayam Penyet", 4.20),
									Item("Mee Rebus", 2.80),
									Item("Mee Siam", 2.80)],
					1.6, "0800". "2000")

directory = [noodle_stall]
"""
    Things to do:
        Hard code all the starting data for the app
            - all the stalls and the items that they sell
        Create an Array of all the stalls and call it directory
"""
