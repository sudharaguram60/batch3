'''
#! eg:3
#take values of length and breadth of a
#from user and chek if it is square or not
length=int(input())
breadth=int(input())
if length==breadth:
    print("its a square")
else:
    print("its a not square")
#eg:4
#python program to check whether the
#given integer is a multiple of both 5 and 7
n = int(input("enter the number:"))
if n%5==0 and n%7==0:
    print=("yes")
else:
    prinyt("no")
#eg:5
#write a program to accept to the cost price of a bike and disply the
#road tax to be paid
#according to the follwing criteria:
#costprice(inrs)                    
#>100000
#<100000                                                      
price= int(input("enter the price:"))
total = 0
if price > 100000:
    discount = price*(6/100)
    value = price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is:",total)
'''
'''
#---> if elif else
#eg:1
a=7
b=9
c=30
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")

#a school has following rules for grading system:
#a.below 25 -f
#b.25 to 45-e
#c.45 to 50-d
#d.50 to 60-c
#e.60 to 80-b
#f.above 80-a #ask useer to enter marks and print the corresponding grade.
marks = int(input("Enter marks:"))
if marks<25:
 print ("F")
elif marks>=25and marks<45:
 print ("E")
elif marks>=45and marks<50:
 print ("D")
elif marks>=50and marks<60:
 print ("C")
elif marks>=60and marks<80:
 print ("B")
else:
 print ("A")
#1----> short hand if else
#eg:1
a=9
b=60
if a>b:
     print("a")
else:
    print("b")
    
#-->using short hand if else
#*rules
#1.)statement inside the if condition have to be present at first
#2.)elif cannot be used in short hand if else
#3.)always it have to end with else
 #code to chek the given char is vowel or consonent
char =input("enter the char:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("is a vowel")
else:
    print("its consonent")
#or
str1 ="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonet")
'''
'''
#shorthand if else
char=input("enter the char:")
str1-"aeiouAEIOU"
print("vowels")if char in str1 else print("consonet")
#---->elif ladder using shorthand if else
#eg-1
#find greater among 3 variables using shorthand if else
a=8
b=5
c=9
print ("A is greater")if a>b and a>c else print ("B is greater")
if b>a and b>c else print("C is greater")
'''
'''
#---->looping
#looping can be implimented using
#for loop
#while loop
#--->for loop
for loop is used for iteartion, if we know the number of times the loop have to run
it is used to iteate the iteables eg(string,list,tuple,etc...)
# to do --->syntax for loop
#! for syntax in c
for(1=0;1<10;1++){
    print("hello");
}
'''
'''
#for syntax in python
#for userdefind_variable in range(start,end,step):defalut step value is 1
#statement
#statement
#statement
#eg-1
#to print the values  from 1 to 10 using for loop
for i in range(0,10):
   print(i)
   print("hello")
#eg-2
for val in range(23,50,1):
    print(val)
'''
'''
#eg-3
#to decrement the value
for val in range(10,0,-1):
    print(val)
for val in range(10,0,-2):
    print(val)
for val in range(10,0,1):
    print(val)
'''
'''
#eg-4
#print the output of 7th  mulplication table from 21 t0 43
#num=int(input("display multiplication table of ?"))
for val in range(3,10-3):
     print('7','x',val,'-',val*7)
for val in range(3,10-3):
    ans="7 x {} = {}"
    print(ans.format(val,val*7))
for val in range(3,10-3)
   print(f"7 x {val}={val*7}")
'''
#eg-5
#break---> used to teerminate thje loop
for val in range(1,10):
   print(val)
   if val==6:
       break
for val in range(1,10):
    if val==6:
        print(val)
        break
#continue
#eg-1
for val in range(1,10):
   if val==6:
      continue
   print(val)
#practise problems
#print the even number between 20 to 40
for  val in range(20,41,):
   if val %2==0:
      print(val)



