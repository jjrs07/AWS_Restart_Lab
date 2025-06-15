import json

# Sample Python dictionary
person = {
    "name": "James",
    "age": 30,
    "isCertified": True,
    "skills": ["AWS", "Python", "GitHub"]
}

# Write it to a JSON file
with open('person.json', 'w') as json_file:
    json.dump(person, json_file, indent=4)

print("JSON file written successfully!")

# ✅ Read it back from the JSON file
with open('person.json', 'r') as json_file:
    data = json.load(json_file)

print("Data read from JSON:")
print(data)
