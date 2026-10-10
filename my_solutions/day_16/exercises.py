# Day 16 - time and date

from datetime import datetime

current_date = datetime.now()
print(current_date)
timestamp = current_date.timestamp()
print("timestamp: ",timestamp)
current_date_format = current_date.strftime("%m.%d.%Y, %H:%M:%S")
print(current_date_format)

t_string = "5 December, 2019"
t_object = datetime.strptime(t_string, "%d %B, %Y")
print("t_object = ", t_object)

new_year = datetime(2027,1,1)
print(new_year)

time_to_new_year = new_year - current_date
print(time_to_new_year)
t1 = datetime(1970,1,1)

diff = current_date - t1
print(diff)
