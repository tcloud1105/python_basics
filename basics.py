import datetime
import time
import os
import pandas
'''
 mynow = datetime.datetime.now()
print("the date and time is: ", mynow)

mynumber = 10
mytext = "Hello"
print(mynumber, mytext)
'''


# datatype
x = 10
y = "10"
z = 10.1
student_grade = [12, 23, 67]

sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type(y), type(z), type(student_grade))

# function
def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

print(type(mean), type(sum))

# List comprehension
temps = [221, 234, 340,-9999,  230]

#new_temps = [temp/10 for temp in temps if temp != -9999]
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

# more about functions
def area(a, b=3):
    return a*b

def mean_improve(*args):
    print(type(args))
    print(args)
    return sum(args)/len(args)

def mean_improve2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())/len(kwargs)

print(mean_improve(1,2,4))
print(mean_improve2(a=1,b=2,c=3))

# module
while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as f:
            print(f.read())
            time.sleep(10)
    else:
        with open("files/vegetables.txt","w") as f:
            f.write("macabo")

while True:
    if os.path.exists("files/temps_today.csv"):
        data = panda.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("File not found")
    time.sleep(10)