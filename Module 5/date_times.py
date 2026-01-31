import datetime

# now = datetime.datetime.now()
# print(now)

# today_date = datetime.date.today()
# print(today_date)
# print(now)

# custom_datetime = datetime.datetime(2030,2,10,10,30,0)
# print(custom_datetime)


formatted_date = now.strftime("%Y/%B/%d %I:%M:%S %p")
print(formatted_date)

# ptt = datetime.datetime.strptime(formatted_date, "%Y/%B/%d %H:%M:%S")
# print(ptt)

# print(ptt.strftime("%Y"))

# # timedelta

# from datetime import datetime, timedelta

# current_dt = datetime.now()

# print(current_dt)

# custom_dt = datetime(2025,5,2,9,15)
# print(custom_dt)

# print(current_dt - custom_dt)

# print(current_dt - timedelta(weeks=2))

