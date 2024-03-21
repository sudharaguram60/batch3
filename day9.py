#day-9
#eg-1
'''
#2.)find the common words from 2 strings
#s1= "hello how are you"
#s2 = "hello how is"

s1= "hello how are you"
s2 = "hello how is"
s1 = s1.split(" ")
s2 =  s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
'''
'''
#3.)write a code print the 8th fibnocci number
#0,1,1,2,3,5,5,8

#find the 8th fibnocci number
num = 8
n1 = -1
n2 = 1
for val in range(num):
    ans=n1+n2
    print(ans)
    n1 = n2
    n2 =ans
print(ans)

#constuctors
#eg-2
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()
#eg-3
#parameterrised constuctor
class profile:
    def __init__ (self,id,name,age):.
        print(id,name,age)
obj =profile(1,"kalyan",21)

#eg-4
class c1:
    email = "pavan kalyan"
    def m1(self):
        name = "sneha"
        age = 21
        return name,age
    def display(self):
        #print(name,age)
        #print(self,name,self.age)
        print(self.m1())

object = c1()
object.display()

#eg-5
class class1:
    def __init__ (self):
        self.  name = "sneha"
        self.email = "pavan kalyan"
       #return name,email#error-->cannot use return with constuctor

    def display(self):
        print(self.name,self.email)
c1 = class1()
c1.display()
'''
'''
#----.inheritance
#eg-1
#the process of utilising the methods and attributes of parent class
#throught the object of child class it is called as inheritence
#5 types of inheritence
#single inheritence
#multilevel  inheritence
#multiple  inheritence
#hybid  inheritence
#heiraichal  inheritence

#single  inheritence
#it has only one parent class and only one child class
#eg-1
class parent:
    def m1():
        print("i am parent class")
parent.m1()
class child:
    def m2():
        print("i am child class")
child.m2()

#eg-2
class c1:
     def __init__ (self):
         print("i am constructor from parent class")
class child(c1):
    pass

obj =c1()
'''
'''
#eg-3
class parent:
    name = "sai pallvi"
class child(parent):
    name = "sudha family"
    def display(self):
        print(self.name)
d = child()
d.display()
'''
'''
# multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
 '''
'''
#multiple inheritance
#? it has multiple paremt and 1 child

class while_petrol:
    def function_w(self):
        print("used to Airplane")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
print("Petrols types")

p=petrol()
p.defanition()
p.function()
'''
# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

# ! EXAMPLE:2
class honda_city:
    def honda_city_engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class civic(amaze):
    def civic_engine_spees(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def civic_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class Honda(civic):
    pass
honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# * Multiple Inheritance
# ? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")
class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()
#hybrid inheritance
#the combination of above 4 inheritance is called hybrid

class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")


