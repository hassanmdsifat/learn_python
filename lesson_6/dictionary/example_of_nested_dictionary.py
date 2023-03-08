courses = {
    1: {
        "name": "C",
        "duration": 3
    },
    2: {
        "name": "Python",
        "duration": 4
    }
}

print(courses[1]["name"])
print(courses[2]["duration"])

courses[2]["duration"] = 2
courses[2]["instructor"] = "Sifat Hassan"

print(courses[2])
