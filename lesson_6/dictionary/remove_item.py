employee = {
    "name": "Sifat Hassan",
    "skills": ["Python", "Django", "Go"],
    "years_of_experience": 4,
    "company": "Cefalo Bangladesh Ltd",
    "address": "Dhanmondi",
    "type": "permanent"
}

# del keyword

del employee["type"]

print(employee)

# pop() method
print(employee.pop("address"))
print(employee)