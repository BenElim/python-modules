import my_math
import math, random, string
from datetime import date, datetime
import os
import requests

# custom modules
print(my_math.add(99, 45))
print(my_math.square(55))

# math module
print(math.sqrt(81))

# Random Library
fruits = ["apple", "Banana","cherry","date","mango"]
pick_fruit = random.choice(fruits)
print(pick_fruit)

#Date library
today = date.today()
print(today)
print(datetime.now())

print(string.digits)

# Using OS library/module
current_dir = os.getcwd()
print(current_dir)

# requests library

response = requests.get("https://ciraiq.com/")
print(response.status_code)

