#day-4
#--->while loop
#--->breaking using while loop
'''
#1.)iterate from 20 to 30 and break the loop in 27
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
#2.)
while i<31:
    if i==27:
        break
    print(i)
    i+=1
'''
'''
i = 27
while i<28:
    print(i)
    if i==28:
        break
    i+=1
#-----> continue
i = 20
while i<31:
    i=i+1
    if i==27:
       continue
    print(i)
'
#eg-5
#while to iterate from 12 to 22
i = 12
while i<22:
    print(i)
    i+=1
'''
'''
#find the sum of all numbers
i = 12
sum=0
while i<23:
      sum=sum+i
      i+=1
print(sum)
#eg-6
#find the average of value from 20 to 25
i = 20
sum=0
while i<26:
    sum=sum+i
    avg=sum/6
    i+=1
print(avg)
'''
'''
#----->nested for loop
for row in range(1,3+1):
    for col in range(1,4+1):
        print(row,col)

rows = int(input("enter the rows:"))
cols = int(input("enter the cols:"))
for row in range(rows):
     for col in range(cols):
          print("*", end=" ")
     print()

'''
'''
sum=0
for row in range(5):
     for col in range(5):
         sum=sum+1
     print(sum, end=" ")
     print()
# to print stars in right angled triangle
for row in range(0,6):
    for col in range(row,6):
        print("*", end=" ")
    print()
'''
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#triangle
    
for i in range(1,5+1):
    for j in range(i):
        if j==0 or j==i+1:
            print("*", end=" ")
    else:
        if row !=5:
            print(" ", end=" ")
        else:
            prinr("*", end=" ")

    print()
'''
#---->list
#datatypes
#primary

#number-->int,float complex
#string
#boolean
#none

#collection
#list
#tuple
#set
#dictionary

#--->list
#1.) if the collection of elements are sorounded by squre brakets,it is considerd
#to be list
#eg-:
#l1=[4,7,9,9.89,"hello",7+9j,[8,9,0]]
#characteristices of list
#1.)list have to be sorrounded by[]
#2.)it is mutable(the elements in the list are changable)
#3.)every element inside list is indexed
#4.)the elements inside list will be ordered format
#5.)it can hold duplicate values
#6.)its heterogenous
#to access the elements in the list
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1)
#-->indexing
#in the collection datatyp[es like list ,tuple,string,the elements wii a be allowted
#with pre-defined unique value called index value
#we have 2 types of indexing
#positive indexing--> starts with 0 from left hand side
#negative indexing-->starts with -1 from right hand side
'''
#-->positive indexing
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[0])
print(lst1[4])
print(lst1[20])
'''
'''
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])
#---->slicing
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#3lst1[start_index:end_index:step]
#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[3:])
#print(lst1[:])
#print(lst1[0:7:1])
trail = int(input())
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4])
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])
'''
#to insert ot add element inside list
#append()
l1 = [9,8,0,6]
l1.append("car")
print(l1)




            
    

    
