# A list is a ordered, mutable collection that can store multiple elements and also support duplicate elements.

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)

numbers[1]=10
print(numbers)

#Adding elements to a list
#append
numbers.append(12)
print(numbers)

#extends
numbers.extend([14,16,18])
print(numbers)

#insert
numbers.insert(2,11)
print(numbers)

#Removing elements from a list
#remove
numbers.remove(10)
print(numbers)

#pop
numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

del numbers[11]
print(numbers)

#to clear an entire list
numbers.clear()
print(numbers)

#list Sclicing
#list[start:stop:step]
#The stop index is excluded 

l1=[10,20,30,40,50,60]

print(l1[1:3])
print(l1[2:])
print(l1[:4])
print(l1[::2])
print(l1[1::2])
print(l1[::-1])


#Searching and Checking
l2=[10,20,30,40,50,60,30]
print(30 in l2)
print(100 in l2)

print(l2.index(40))
print(l2.count(30))
print(len(l2))



#Sorting Lists
#sort modifies the original list and return none
# and sorted returns a new list

l3=[10,50,30,70,20,40]
l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)

res=sorted(l3)
print(res)



#Iterating through a list 

l4=[10,20,30,40,50,70,60]
for ele in l4:
    print(ele)
    
for ele in range(len(l4)):
    print(ele,l4[ele])
    

for ind,ele in enumerate(l4):
    print(ind,ele)
    
    
    
#Nested Lists
l5=[[10,20,30],[40,50,60],[70,80,90]]

#accessing values
print(l5[0])
print(l5[2][1])






## List Copying

a=[10,20,30]
b=a
b.append(40)
print(a)
print(b)
# both outputs will be same because both a and b are poinitng to the same list in memory.


#This is Shallow copy.
c=[10,20,30]
d=c.copy()
d.append(40)
print(c)
print(d)

#we can also use this
d=c[:]
print(d)
d=list(c)
print(d)