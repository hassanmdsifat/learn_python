employee = {
    "name": "Sifat Hassan",
    "skills": ["Python", "Django", "Go"],
    "years_of_experience": 4
}

# employee["name"] = "Test User"
# employee["years_of_experience"] = 8

# .update()

employee.update(
    {
        "name": "Test User",
        "years_of_experience": 8
    }
)
print(employee)