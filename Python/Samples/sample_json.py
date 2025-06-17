import json
filename = 'user.json'
name = ''
try:
    with open(filename, 'r') as r:
        name = json.load(r)
except IOError:
    print("First-time login")

if name != "":
    print("Welcome back," + name + "!")

else:
    name = input("Hello! What's your name? ")
    print("Welcome, " + name + "!")
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("Error writing to file")  