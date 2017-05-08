
# coding: utf-8

# In[ ]:

#------------operations------------

#sum
print(2 + 1)

#subtraction
print(3 - 2)

#multiplication
print(2 * 2)

#power
print(2 ** 2)

#divisions
print(4 / 2.0)
print(int(4 / 2))
print(type(str(4/2)))

#mod
print(5 % 2)
print(5 % 1)


# In[ ]:

#------------variable type------------

#int
integer_var = 12

#double
double_var = 2.5

#string
'I am a string' "I am a string"

#boolean
a = 2
b = 3
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a>b and b==b)
print(a>b or b==b)


# In[ ]:

#------------Print------------
x = 'I am a string'
print(x)

#formatting strings
age  = 19
sex = "girl"
country = "USA"
name = "Kelly"

print("My name is {} and I am {} years old. I am a {} from {}".format(name,age,sex,country))
print("My name is {name} and I am {age} years old. I am a {sex} from {country}".format(name=name,age=age,sex=sex,country=country))

#string are an array of characters 
string = "I am another string"
string[5]
string[1:5]
string[5:]
string[:5]



# In[ ]:

#------------List------------
#enumerated list 0,1,2,3,4
#mixed data type

list1 = ["USA", 99, "guns"]
list2 = [44,77,87.7,55]

#len 
print(len(list1))

#type
print(type(list1))

#max
print(max(list2))

#min
print(min(list2))

#sort
list2.sort()
print(list2)

#Adding items to a list
list1.append("chocolate")
print(list1)

#removing items from a list
print("removed: "+ str(list1.pop(1)))
print(list1)

#check an item inside a list
print("x" in ["x",88,"Torino"])



# In[ ]:

#------------Dictionaries------------

dictionary1 = {"key1":"Ferrari","key2":"Mercedes"}
dictionary2 = {"key1":[14,77,54],"key2":"Mercedes"}
dictionary3 = {"key1":{"numbers":[55,43,99]},"key2":"Mercedes"}

#Accessing values inside a nested dictionary
print(dictionary3["key1"]["numbers"][2])

#some extra things you can do with the dictionaries
print(dictionary1.keys())
print(dictionary1.items())
print(dictionary1.values())




# In[ ]:

#------------Set------------
set1 = {1,2,6,7,5,5}
set1.add(9)
set1




# In[ ]:

#------------Touples------------

#touples are immutable 
tup1 = ("moon", "venus", 2017, 2009)

#Operation on list of touples
num = [(0,1),(1,1),(0,0)]
for a,b in num: print(a)


# In[ ]:

#------------List vs Touples vs Dictionaries------------
list1 = []
touples1 = ()
disctionaries = {}
 


# In[ ]:

#------------if elif else------------

a = 10
b = 20

if a == b:
    print("Something is wrong here")
elif b == b:
    print("How obvious")
else:
    print("uhm")


# In[ ]:

#------------for while range------------

age_set=[33,56,78,92,11]
for numbers in age_set:
    print("Someone has {} years old".format(numbers))
    print("Increment the age of {} + 1 -> ".format(numbers)+ str(numbers+1)) 

for numbers in list(range(1,10)):
    print(numbers)
    
print(list(range(5)))
    
a = 1
while a < 10:
    print("a is {}".format(a))
    a = a + 1


# In[ ]:

#------------Appending items to a list with a for loop------------

my_list = []
for numbers in range(10):
    my_list.append(numbers **2)
print(my_list)

#List Comprehensions
print([numbers **2 for numbers in range(10)])
print([numbers **2 for numbers in range(10) if numbers % 2 == 0])


# In[ ]:

#------------functions------------

def welcome(name = "{error: name not assigned}"):
    print("hello {}".format(name))

welcome("MindwareLab")
welcome()

def power(numbers, power):
    return numbers **power

output = power(10,2)
power(7,37)

print(output)




# In[ ]:

#------------Maps and lambda------------
from functools import reduce
list_of_number = [1,2,3,4,5,6,7,8,9,10]

#maps a function
def power2(num):
    return num **2
print(list(map(power2,list_of_number)))

#labda functions 
print(list(map(lambda n: n**2, list_of_number)))
print(list(map(lambda n: n**2, range(11))))

#Filters
print(list(filter(lambda x: x<=5, list_of_number)))
print(list(filter(lambda x: x%2 == 0, list_of_number)))
print(list(filter(lambda x: x%2 == 1, list_of_number)))

#Reduce
print(reduce((lambda x, y: x*y), [1,2,3,4,5,6,7,8,9,10]))
print(reduce((lambda x, y: x*y), list_of_number))


# In[ ]:

#------------String formatting------------

website = "http://www.MINdwareLaB.org"

print(website.upper())
print(website.lower())
print(website.split("."))
print(website.split("//"))
print(website.split("www"))
print(website.split(".")[1])
print(website.split(".")[2])


# In[18]:

#----------Classes-----------
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@mindwarelab.com"
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def increse_salary(self):
        self.pay =  int(self.pay + 10)

#creating a new employee
employee1 = Employee("Frak","Lasagna", 10)

#Accessing Attributes
print(employee1.email.lower())
print(employee1.fullname())
print(employee1.pay)

#increase the salary
employee1.increse_salary()
print(employee1.pay)

        


# In[ ]:



