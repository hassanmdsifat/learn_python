from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

# 11/03/2023 15:36:55

# strftime() method

print(datetime.strftime(current_datetime, "%d/%m/%Y %H:%M:%S"))