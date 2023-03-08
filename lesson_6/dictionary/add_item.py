employee = {
    "name": "Sifat Hassan",
    "skills": ["Python", "Django", "Go"],
    "years_of_experience": 4
}

employee["company_name"] = "Cefalo Bangladesh Ltd"

employee.update({
    "address": "Dhanmondi",
    "type": "permanent"
})

print(employee)