import datetime as dt

yesterday = dt.datetime.now() - dt.timedelta(days=1)
today     = dt.datetime.now()
tomorrow  = dt.datetime.now() + dt.timedelta(days=1)

print(yesterday.strftime("Yestarday : [%Y - %m - %d]"))
print(today.strftime    ("Today     : [%Y - %m - %d]"))
print(tomorrow.strftime ("Tomorrow  : [%Y - %m - %d]"))