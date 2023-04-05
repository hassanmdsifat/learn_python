import datetime

class TimeUtilityManager:

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now()

    @staticmethod
    def get_date_difference(date_from):
        return datetime.datetime.now() - date_from


print(TimeUtilityManager.get_current_datetime())

current_date = datetime.datetime(2019, 3, 3)

print(TimeUtilityManager.get_date_difference(current_date))