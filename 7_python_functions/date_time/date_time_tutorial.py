import datetime

# current_datetime print

print(datetime.datetime.now())

# current_utc time

print(datetime.datetime.utcnow())

# get today

print(datetime.date.today())

# timestamp

random_date = datetime.date.fromtimestamp(12345678)
print(random_date.year)
print(random_date.month)
print(random_date.day)