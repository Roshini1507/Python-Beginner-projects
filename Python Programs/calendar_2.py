#To display all the months of the given year

import calendar

year = int(input("Enter the year: "))
x = calendar.calendar(year)
print(x)