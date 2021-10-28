#Any year is entered through the keyboard, write a program to
#determine whether the year is leap or not. Use the logical
#operators and ,or.

#year=int(input("Enter the year to check: "))

# leap year is divisible by 4 but not by 100
""" def div_by_4(n):
    return (((n>>2)<<2)==n)
#def div_by_100(n):
    
num=int(input("enter the number to check dvisibility by 4: "))
print(div_by_4(num)) """

import datetime
start=datetime.datetime(day=1,month=10,year=2021).date()
end=datetime.datetime(day=1,month=11,year=2021).date()
current = datetime.date.today()
print(start)
print(end)
print(current)

def time_in_range(start, end, current):
    return start <= current <= end
print(time_in_range(start,end,current))
