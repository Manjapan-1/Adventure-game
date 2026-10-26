# Money Functions

import random

def purchase_item(Item_Price, Starting_Money, Quantity_To_Purchase=1):
   
    Max_Affordable = Starting_Money // Item_Price
    num_Purchased = min(Quantity_To_Purchase, Max_Affordable)
    Left_Over = Starting_Money - num_Purchased * Item_Price
    return num_Purchased, Left_Over

# Monster Functions

def new_random_monster():
    monsterTypes = [
        {
            "name": "Vampire",
            "description": "This is a Vampire, a creature of the night, when it notice you, it lunges at you"
                           "Quickly with Fangs drawn",
            "health": (20, 40),
            "power": (8, 16),
            "money": (12, 14),
        },
        {
            "name": "Condor",
            "description": "This is a Condor, a creature of flight, when it notice you, it swoops down at you"
                           "Quickly with Tallons drawn",
            "health": (15, 30),
            "power": (3, 8),
            "money": (5, 25),
        },
        {
            "name": "SlimeCube",
            "description": "This is a SlimeCube, a creature of great mass, when it notice you, it does nothing"
                           "Quickly it stays still",
            "health": (10, 20),
            "power": (4, 8),
            "money": (13, 16),
        },
    ]

    Chosen = random.choice(monsterTypes)
    return {
        "name": Chosen["name"],
        "description": Chosen["description"],
        "health": random.randint(*Chosen["health"]),
        "power": random.randint(*Chosen["power"]),
        "money": random.randint(*Chosen["money"]),
    }

# Demonstration Code

print("=== Purchase_Item()===")

# Can Afford What Was Requested

num_Purchased, Left_Over = purchase_item(50, 200, 3)
print(f"Purchased {num_Purchased}, Money Left {Left_Over}")

# Wants More But Only Can Purchase One

num_Purchased, Left_Over = purchase_item(50, 80, 3)
print(f"Purchased {num_Purchased}, Money Left {Left_Over}")

# Quantity To Purchase

num_Purchased, Left_Over = purchase_item(77, 2012)
print(f"Purchased {num_Purchased}, Money Left {Left_Over}")

# Demonstration Monster Code

print()
print("=== new_random_monster() ===")

for i in range(3):
      My_Monster = new_random_monster()
      print(f"Monster {i + 1}: {My_Monster['name']}")
      print(f"  Description: {My_Monster['description']}")
      print(f"  Health: {My_Monster['health']}")
      print(f"  Power: {My_Monster['power']}")
      print(f"  Money: {My_Monster['money']}")
      
       
      









        

        
  
    
