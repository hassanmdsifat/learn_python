# .replace(oldvalue, newvalue, count)

"""The replace() in Python returns a copy of the string
where all occurrences of a substring are replaced with another substring.
"""

welcome_text = "Welcome to Python!!!Python Python"

modified_welcome_text = welcome_text.replace("!", "#", 1)

print(modified_welcome_text)