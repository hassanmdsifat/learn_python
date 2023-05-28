# strptime()

from datetime import datetime

book_creation_date = "03, March, 2023"

book_creation_actual_date = datetime.strptime(book_creation_date, "%d, %B, %Y")
print(type(book_creation_actual_date))
print(book_creation_actual_date)