"""
.format()
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}
The placeholders can be identified using
    - named indexes {price},
    - numbered indexes {0},
    - empty placeholders {}.
"""

first_name = "Sifat"
last_name = "Hassan"
user_id = 14

full_name = "{first_name} {last_name} and user id is {user_id}" \
            "".format(
    first_name=first_name,
    last_name=last_name,
    user_id=user_id
)
print(full_name)

