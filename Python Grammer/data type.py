print(type("jing hui"))
print(type(888))
print(type(79.53))

# type
name = "jing hui"
name_type = type(name)
print(name_type)


# transfer string to int
num_str = str(11)
print(type(num_str), num_str)

# transfer string to number
float_str = str(11.88)
print(type(float_str), float_str)
num = int("11")
print(type(num), num)
num = float("11.88")
print(type(num), num)

# code identifier
name_ = "jing hui"
_name = "jing hui"
name_1 = "jing hui"
Itheima = "jing hui"
itheima = "888"
print(name_)

firstnumber = 8
studentnickname = "jing hui" 

first_number = "8"
student_nickname = "jing hui"
print(first_number, student_nickname)

# if pattern

age = 30
if age >= 18:
    print("adult")

age = int(input("input your age:"))

# if for adult or not
if age >= 18:
    print("adult, pay 10$ more")
else:
    print("Enjoy the trip")

# height data
height = int(input("input your height(cm):"))
if height >= 120:
    print("pay 10$ more")
else:
    print("Enjoy the trip")


# if elielsef  pattern 

# the 1st if
if int(input("input your height(cm):")) < 120:
    print("Enjoy the trip")
elif input("input your vip level(1-5):") > 3:
    print("enjoy your trip")
elif int(input("input your day:")) == 1:
        print("Free trip")
else:
    print("pay 10$ more")
    

    