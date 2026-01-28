#this program prompts the user for their name and then greets them 
name = input("What is your name? ")

clean = " ".join(name.split()).title()

print(f"Hello, {clean}!")

