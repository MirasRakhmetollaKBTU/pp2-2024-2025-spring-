import datetime as dt

current_day = dt.datetime.now()

current_day_without_mcrsecunds = current_day.replace(microsecond=0)

print("Day with microseconds    ", current_day)
print("Day without microseconds ", current_day_without_mcrsecunds)
