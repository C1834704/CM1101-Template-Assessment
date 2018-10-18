from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

# Maximum mass of items you can carry at any given time (kg)
max_carry_mass = 3.0
