import time
import sys

def write(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x

write("This is a greatest common denominator calculator.\n")
time.sleep(1)
write("The calculator will find the greatest common \ndenominator of your two inputted numbers.\n")
number1 = int(input("First Number > "))
number2 = int(input("Second Number > "))
write("The greatest common denominator of your numbers is...\n")
print(gcd(number1,number2))
