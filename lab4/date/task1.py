import datetime as dt

current_day = dt.datetime.now()
new_date    = current_day - dt.timedelta(days=5)

print(current_day.strftime("%Y - %m - %d"))
print(new_date.strftime("%Y - %m - %d"))