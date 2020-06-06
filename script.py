# Simple Python Script
# vscode creates own settings file in here
# We're going to edit globale user settings
# Use black formatter
# Sort imports
# Enable pylint
# Run any input stuff in terminal
# import math
# import sys
# from os import rename

import requests

# What version of python?
# print(sys.version)
# Where it's located?
# print(sys.executable)


# def greet(who_to_greet):
#     greeting = "Hello, {}".format(who_to_greet)
#     return greeting


# print(greet('World'))
# print(greet('Abhishek'))

# Check that requests is working
r = requests.get("https://github.com/factorwonk")
# Add a break point around here
print(r.status_code)

# name = input("Your name? ")
# print("Hello, ", name)
