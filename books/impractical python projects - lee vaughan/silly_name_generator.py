import sys, random

first_name_start = ("Do", "Re", "Mi", "Fa", "So", "La", "Si")
first_name_end = ("do", "re", "mi", "fa", "so", "la", "si")

print("Welcome to a random name generator")

repeat = ""

while repeat != "n":
	first_name = random.choice(first_name_start) + random.choice(first_name_end)
	last_name = random.choice(first_name_start) + random.choice(first_name_end)

	print(f"\nYour name is {first_name} {last_name}")

	print("\n\nWould you like to generate another name?? (Enter 'n' for no')")
	repeat = input(": ")

print("\n\nPress enter to quit")
