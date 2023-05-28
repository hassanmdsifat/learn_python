employee = {
    "name": "Sifat Hassan",
    "skills": ["Python", "Django", "Go"],
    "years_of_experience": 4
}

print(employee["name"])
print(employee["skills"])

# print(employee["salary"])

# get()

print(employee.get("salary", "Not found!!!"))