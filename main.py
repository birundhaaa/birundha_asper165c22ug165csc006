 # implement a recursive function to calculate the factorial of a given number.

"""
1! = 1 x 1
2! = 2 x 1! --->2 x 1
3! = 3 x 2! --->3 x 2 x 1
.
.
10! = 10 x 9! --->10 x 9 x 8 x... x 1

formula - n x (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number = 6
res = fact_rec(number)

print("the factorial of {} is {}".format(number,res))
# Leap year

"""
year % 4 = 0
year % 100 != 0/
year % 400 == 0

"""
def isLeapYear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = 2020

if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not leap year.'.format(year))