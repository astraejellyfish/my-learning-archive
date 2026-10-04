#NOTE! if you're gonna run this make sure to multi coment first

# assigning multiple variables in one line
"""coffee = "latte"
print (a); print (b); print (c)

#unpacking a collection
coffee = ["latte", "cappuccino", "americano"]
a, b, c = coffee
print (a); print (b); print (c)

#output variables
a="flins"; b="is"; c="pogi"
print (a,b,c)

a=15; b=16
print(a + b)

#Global Variables
a="pogi"

def myfunc():
    a="twink"
    print("Flins is " + a)
myfunc()
print("Scara is " +a)

#the global keyword is used to create a global variable inside a function
def myfunc():
    global a
    a="pogi"

myfunc()
print("Flins is " + a)

#numeric types in python
x = 1 # integer
y = 2.8 # float
z = 1j # complex

#python casting
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x); print(y); print(z)

#strings are arrays
a = "flins, pogi"
print(a[0]) #first character
print(a[1]) #second character
print(a[2]) #third character and so on

#lopping through a string
for x in "flins":
    print(x) #output each character in the string one by one
#length
a = "flins is handsome"
print(len(a)) #output the length of the string is 17 characters
"""
#check string
txt = "flins is pogi"
if "pogi" in txt:
    print("yes super pogi")
else:
    print("eekkkk")
   