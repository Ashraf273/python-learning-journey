# Create a list containing 10 integers and print every element.
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for ele in l1:
    print(ele,end=' ')
print()



# Find the sum of all elements without using sum().
numbers = [45, 12, 89, 34, 7, 56]
total = 0

for num in numbers:
    total += num

print(total)


# Find the largest and smallest elements without using max() or min().
numbers = [45, 12, 89, 34, 7, 56]
largest=numbers[0]
smallest=numbers[0]

for ele in numbers:
    if ele>largest:
        largest=ele
    if ele<smallest:
        smallest=ele

print("Largest:", largest)
print("Smallest:", smallest)



# Count how many even and odd numbers exist in a list.
count=0
for ele in l1:  
    if ele%2==0:
        count=count+1
print("The count of even ele's in list is",count)
print("The count of odd ele's in the list is ",len(l1)-count)


    
# Reverse a list without using reverse() or slicing.
numbers = [30, 10, 50, 20, 40]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)



# Find the second-largest element in a list.
numbers = [10, 20, 30, 40, 40]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)




# Remove all duplicate elements from a list.
numbers = [1, 2, 2, 3, 1, 4, 3]

unique = []

for num in numbers:

    if num not in unique:
        unique.append(num)

print(unique)




# Move all zeros to the end without changing the relative order of other elements.
numbers = [1, 2, 0, 3, 0, 5, 0, 0, 6]

result = []

zero_count = 0

for num in numbers:

    if num == 0:
        zero_count += 1
    else:
        result.append(num)

result.extend([0] * zero_count)

print(result)




# Find the frequency of each element.
freq=0
for ele in set(l1):
    freq=l1.count(ele)
    print(f"The frequency of {ele} is {freq}")



# Merge two lists and sort the resulting list without modifying the original lists.
l3=[1,2,3,4,5]
l4=[6,7,8,9,10]
l5=l3+l4
l5.sort()
print(l5)






#Find the missing number from a list containing numbers from 1 to N.
m=[1, 2, 3, 5, 6]
for ele in range(0,len(m)-1):
    if m[ele]+1!=m[ele+1]:
        print("The missing number is",m[ele]+1)

#Find all duplicate elements in a list.
freq=0
for ele in set(l1):
    freq=l1.count(ele)
    if freq>1:
        print(f"The duplicate element is {ele} and its frequency is {freq}")




#Rotate a list to the right by K positions.
lk=[1, 2, 3, 4, 5]  
k=2
lk=lk[-k:]+lk[:-k] #[4,3,2,1] +[5] => [4,5,1,2,3]
print(lk)



#Separate positive and negative numbers.
lis=[-1, 2, -3, 4, -5, 6]
pos=[]
neg=[]
for ele in lis:
    if ele>0:
        pos.append(ele)
    else:
        neg.append(ele)

print("Positive numbers:", pos)
print("Negative numbers:", neg)


#Find pairs whose sum equals a given target.
lis1=[1, 2, 3, 4, 5,6,7,8,9,10]
target=10
pairs=[]
s=set()

for ele in lis1:
    com=target-ele
    if com in s:
        pairs.append((com,ele))
    s.add(ele)
print(pairs)




#Find the intersection of two lists without using sets.
il1=[1, 2, 3, 4, 5]
il2=[4, 5, 6, 7, 8]
inter=[ele for ele in il1 if ele in il2]
print(inter)


#Find the union of two lists without duplicates.
ul1=[1, 2, 3, 4, 5]
ul2=[4, 5, 6, 7, 8]
union=ul1+[ele for ele in ul2 if ele not in ul1]
print(union)



#Flatten a nested list.
nl=[[1, 2], [3, 4], [5, 6]]
fl=[ele for sl in nl for ele in sl]
print(fl)


#Find the third-largest distinct element.
l=[10, 20, 30, 40, 40, 50]
fl=0
sl=0
tl=0
for ele in set(l):
    if ele>fl:
        tl=sl
        sl=fl
        fl=ele
    elif ele>sl:
        tl=sl
        sl=ele
    elif ele>tl:
        tl=ele  
print(tl)



#Find the maximum sum of a contiguous subarray.




 #Advanced – 5 questions
 # Find the longest consecutive sequence in an unsorted list.
 # Find the most frequently occurring element.
 # Find all triplets whose sum equals zero.
 # Rotate a matrix by 90 degrees.
 # Find the product of all elements except the current element, without using division.