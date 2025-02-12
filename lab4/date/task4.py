import datetime as dt

first_date  = input("Enter first date [YYYY-MM-DD] : ")
second_date = input("Enter first date [YYYY-MM-DD] : ")

date1 = dt.datetime.strptime(first_date, "%Y-%m-%d")
date2 = dt.datetime.strptime(second_date, "%Y-%m-%d")

difference = abs((date1 - date2).total_seconds());
print(f"difference between {first_date} and {second_date} is seconds in {difference:.0f}")
