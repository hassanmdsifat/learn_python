import datetime

current_date_time = datetime.datetime.now()

sturct_time_obj = current_date_time.timetuple()
print(sturct_time_obj[0])
print(sturct_time_obj[1])
print(sturct_time_obj[2])