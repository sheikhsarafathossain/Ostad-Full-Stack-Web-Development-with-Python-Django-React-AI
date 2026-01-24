from datetime import datetime, timedelta


today = datetime.today().date()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(today,tomorrow,yesterday)

now = datetime.today()
print(now)
new_time = now + timedelta(hours=5, minutes=30)
print(new_time)