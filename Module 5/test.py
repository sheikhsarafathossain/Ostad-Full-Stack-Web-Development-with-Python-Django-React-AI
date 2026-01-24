import addTwoNum as atn
from addTwoNum import add,sub
# total = atn.add(5,10)
# print(total)
print(add(4,3))
print(sub(5,3))
#package is collection 

print(__name__)
import datetime

now = datetime.datetime.now()
print(now)

today_date = datetime.date.today()
print(today_date)
print(now)

custom_datetime = datetime.datetime(2030,2,10,10,30,0)
print(custom_datetime)

print("-------")
formatted_date = datetime.datetime.now().strftime("%d-%B-%Y %I:%M:%S %p")
print(formatted_date)
ss = datetime.datetime.strptime(formatted_date,"%d-%B-%Y %I:%M:%S %p")
print(ss)
print(type(ss), type(formatted_date))