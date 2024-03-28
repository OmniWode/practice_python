#01_character_input.py

name = input("What is your name? ")
age = input("What is your age? ")
year = 2024 + (100 - int(age))
print(name + ",  you will be 100 years old in " + str(year))