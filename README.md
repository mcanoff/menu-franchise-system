# Menu Simulation

This project demonstrates how to use the `Menu` class to create menus with items, prices, and times, as well as calculate bills for purchased items.

## Usage Example

"""python
from datetime import time
from menu import Menu

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'coffee': 1.50}
brunch_menu = Menu("Brunch", brunch_items, time(11, 0), time(14, 0))

print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'coffee']))
"""
