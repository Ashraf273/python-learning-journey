numbers=(10,20,30,40,50)
print(numbers)
print(type(numbers))

#numbers[0]=100 #TypeError: 'tuple' object does not support item assignment

#empty tuple
empty_tup=()

#tuple with intergers
int_tup=(10,20,30)

#tuple with strings
str_tup=("apple","banana","cherry")

#tuple with mixed data types
mix_tup=(10,"apple",True,3.14)

#without parentheses
tup=10,20,30

# ****  Python recognises tuples primarily through the comma, not the parentheses. **** #

a = (10)
print(type(a)) # output: <class 'int'> why? Because (10) is simply an integer inside parentheses.

#To create a single-element tuple:
a = (10,)
print(type(a))



languages = ("Python", "Java", "C++", "SQL")
print(languages[0])
print(languages[2])
print(languages[-1])


print(languages[1:3])
print(languages[::-1])

#Tuples have only two built-in methods.
#count() – Counts how many times an element occurs.
n=(10,20,10,10,40,10)
print(n.count(10))

#index() – Returns the index of the first occurrence.
numbers = (10, 20, 30, 20)
print(numbers.index(20))
#If an element doesn't exist, index() raises a ValueError.


numbers = (10, 20, 30, 40)
for num in numbers:
    print(num)
    
for index,num in enumerate(numbers):
    print(f"Index: {index}, Value: {num}")
    

numbers = (10, 20, 30)
numbers = (100,) + numbers[1:]
print(numbers)

data=(10,20,[30,40])
data[2].append(50)
print(data)



#Tuple packing and unpacking
  #Packing: Putting multiple values into one tuple.
student = "Ashraf", 23, "Python"
print(student)

  #Unpacking: Extracting tuple values into separate variables.
student = ("Ashraf", 23, "Python")
name, age, language = student
print(name)
print(age)
print(language) 
#The number of variables must match the number of tuple elements unless you use extended unpacking   

#Extended unpacking using *
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

print()
#Nested TUples :  A tuple can contain other tuples as elements, creating a nested structure.

students = (
    (101, "Ashraf", 85),
    (102, "Rahul", 90),
    (103, "John", 78)
)
print(students[0])
print(students[0][1])
print(students[1][2])

for student in students:
    student_id, name, marks = student
    print(student_id, name, marks)
    
    
#Use tuples when:

#- The collection represents a fixed record.
#- You don't want accidental modifications.
#- You want to return multiple values from a function.
#- You need an immutable object that can be used as a dictionary key, provided all its elements are hashable.


location = (12.9716, 77.5946)

locations = {
    (12.9716, 77.5946): "Bengaluru",
    (17.3850, 78.4867): "Hyderabad"
}
#A tuple containing a list cannot be used as a dictionary key because it is not hashable.










#Create a tuple containing 10 integers and print all elements.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for n in numbers:
    print(n)


#Find the length of a tuple without using len().
length=0
for i in numbers:
    length+=1
print(length)


#Find the largest and smallest elements without using max() or min().
l=numbers[0]
s=numbers[0]
for i in numbers:
    if i>l:
        l=i
    elif i<s:
        s=i
print("Largest:",l)
print("Smallest:",s)


#Count how many times a given element appears.
num=(10,20,30,10,40,10)
count=0
for i in num:
    if i==10:
        count+=1
print("Count of 10:",count)

#Reverse a tuple without using slicing.
rev_num=()
for i in range(len(num)-1,-1,-1):
    rev_num+=(num[i],)
print(rev_num)
    
#Check whether an element exists in a tuple without using in.
for i in num:
    if i==30:
        print("30 exists in the tuple")
        break
    


#Convert a tuple into a list, modify the second element, and convert it back into a tuple.
num=(10,20,30,40)
num_list=list(num)
num_list[1]=25
num=tuple(num_list)


#Unpack this tuple into separate variables:
employee = (101, "Ashraf", "Data Engineer", 30000)
emp_id,emp_name,emp_role,emp_sal=employee
print("emp id:",emp_id,"emp name:",emp_name,"","emp role:",emp_role,"","emp salary:",emp_sal)


#Find the second-largest distinct element without sorting.
numbers = (10, 40, 20, 40, 30, 10)
largest = float('-inf')
second_largest = float('-inf')
for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i


#Given a nested tuple, print the name of the student who scored the highest marks.
students = (
    (101, "Ashraf", 85),
    (102, "Rahul", 92),
    (103, "John", 78)
)
highest_student = students[0]
for student in students:
    if student[2] > highest_student[2]:
        highest_student = student
print("Student with highest marks:", highest_student[1])



#Given two tuples, find their common elements without using sets.

tup1=(10, 20, 30, 40)
tup2=(30, 40, 50, 60)
comm=()
for i in tup1:
    if i in tup2:
        comm+=(i,)
print("Common elements:",comm)



#Write a function that returns the minimum, maximum, and average of a tuple.

tup=(10, 20, 30, 40, 50)
def min_max_avg(t):
    min=t[0]
    max=t[0]
    sum=0
    for i in t:
        if i<min:
            min=i
        elif i>max:
            max=i
        sum+=i
    avg=sum/len(t)
    return "Min is "+str(min), "max is "+str(max), "Avg is "+str(avg)

res=min_max_avg(tup)
print(res)


#Given a tuple of integers, return a new tuple containing only unique elements while preserving their original order.

tuple=(10, 20, 30, 20, 40, 10, 50)
def unique_tuple(t):
    unique=()
    for i in t:
        if i not in unique:
            unique+=(i,)
    return "Unique eles are "+str(unique)
res=unique_tuple(tuple)
print(res)
            

#Explain why this code works even though tuples are immutable:
data = (10, 20, [30, 40])
data[2].append(50)

#Because the tuple itself is immutable, meaning you cannot change which objects are in the tuple. However, if the tuple contains a mutable object (like a list), you can modify that mutable object. In this case, `data[2]` is a list, and you can append to that list even though the tuple itself cannot be changed.

#Explain the difference between these two:
a = (10)
b = (10,)
#The first one, `a = (10)`, is just an integer wrapped in parentheses, so `a` is of type `int`. The second one, `b = (10,)`, is a tuple with a single element, so `b` is of type `tuple`. The comma is what makes it a tuple.