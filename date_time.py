from datetime import datetime

now = datetime.now()

print("now:", now)

# year = now.year
# month = now.month
# day = now.day

# print("year:", year)
# print("month:", month)
# print("day:", day)

print("formatted:", now.strftime("%Y-%m-%d %I:%M"))

# tomorrow = datetime(2024, 2, 29)
# print("tomorrow:", tomorrow)
