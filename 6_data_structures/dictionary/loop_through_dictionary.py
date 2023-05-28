employee = {
    "name": "Sifat Hassan",
    "skills": ["Python", "Django", "Go"],
    "years_of_experience": 4,
    "company": "Cefalo Bangladesh Ltd",
    "address": "Dhanmondi",
    "type": "permanent"
}
# keys()
print(employee.keys())

# values()
print(employee.values())

# items()
print(employee.items())


for current_key in employee.keys():
    print(current_key, employee[current_key])


for key, value in employee.items():
    print(key, value)