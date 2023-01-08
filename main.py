from math import*
#strings and veriables
person_name="mr jack"
object_one="car"
print("Hello "+person_name)
print("this "+object_one+" is mine")
person_name="mr rock"
object_one="mobile"
print("Hello "+person_name)
print("this "+object_one+" is mine")
#boolean
having_a_house=False
if having_a_house:
    print("Verified")
#string menipulation
print("I love pizza")
sentence="i love PPPizza and nachos"
print(sentence.lower().islower())

print(len(sentence))

print(sentence.replace("love","hate"))

print(sentence.index("nachos"))


print("word")

#math 

print(10+10*3)
age=25
print("my age is "+str(age))


print(max(1,2,4,2,3,40))
print(min(1,2,4,2,3,40))

print(sqrt(round(pow(5,2))))


print(ceil(23.000001))

#understanding input

#age=input("what is your age:")

#print("my age is"+age)


#functions

def love(name):
    print("I love "+name)

love("pizza")


def person1(name):
    print(name+" : hello how can I help you?")


"""

def person2(food,drink,desert,name):
    name = input("What is your name")
    food = input("What type of food do you want?")
    drink = input("What do you wnat to eat?")
    desert = input("What desert do you want?")

    print(name+": I would like "+food+" I want to drink"+drink+" I want "+desert+" as desert")






person1("Waiter")
person2("food","drink","desert","name")
"""
def calculation(a,b,c):
    print(a)
    print(b)
    print(c)
    return print(a+b+c)
    

"""""
x=int(input("enter value for a:"))
y=int(input("enter value for b:"))
z=int(input("enter value for c:"))
print(x)
print(y)
print(z)
calculation(x,y,z)
"""
###if statments

I_want_to_eat=False
I_want_to_drink=True

if not I_want_to_eat:
    print("Let's have a pizza")
elif I_want_to_drink:
    print("Let's drink")    
else: print("I'm good")

var1=3
var2=3
var3=3
if var1==var2==var3:
    print("yes")
else:
    print("no")

