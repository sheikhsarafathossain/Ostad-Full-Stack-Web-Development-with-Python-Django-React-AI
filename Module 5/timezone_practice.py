import pytz, datetime
import time
dhaka_timezone = pytz.timezone("Asia/Dhaka")
utc =  datetime.datetime.now(datetime.UTC)
print(utc.astimezone(dhaka_timezone))
print(utc)


print(pytz.all_timezones)

start = datetime.datetime.now()
time.sleep(5)
end = datetime.datetime.now()
print(end-start)