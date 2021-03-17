"""x=30
y=3.20
b=0b1010
h=0x1234
o=0o67
print(x,y,b,h,o)
print("x is ",type(x),"\n y is ",type(y),"\n b is ",type(b),"\n h is ",type(h),"\n o is ",type(o))

#type Casting
print("binary to float: ",float(b))
"""

#String creation
str1="10"
str2="20"
str3="""highs
        jfhvlgf"""
print(str1)
print(str2)
print(str3)
str1.isupper()
#string concatination
print("concatinated string: ",str1+str2)
print(str2*4)

#slicing
#Accessing string characters in Python
str = 'python programing'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#iterating Sting
for c in str:  
    print(c)

"""
"""
#List
list1=[39,298,90]
print("initial list: ",list1)

#Insert using append, extend, insert
list1.append("Hemlata")
list1.append(("using","append"))
print("after appending list: ",list1)
list1.extend(("using","extend"))
print("after extending list: ",list1)
list1.insert(5,"using Insert")
print("after inserting into list: ",list1)

#deleting elements
list1.remove("using");
list1.pop(4)
list1.pop(3)
list1.pop(4)
list1.pop(3)
print("list after delete ",list1)

#sorted and Sort
print("Sorted List: ",sorted(list1))
print("actual list after sorted: ",list1)
list1.sort()
print("actual list after sort ",list1)
"""
"""
#tuple
tuple1 = (1,2,3)
print("initally created tuple ", tuple1)

#add ite to tuple (we use concatination)
tuple1 += (4,5,6,)
print("elements added to tuple' ",tuple1)

dict1={1:"Java",2:"python"}
print(dict1)
#dict is mutable
dict1[1]="spring boot"
print(dict1)

#add value to dict
dict1[3]="dbms"
print(dict1)

#dete item from dict
del dict1[2]
print(dict1)

print("all keys in dict: ",dict1.keys())
print("all items in dict: ",dict1.items()) 

#SET
set1= {1,2,3,4,5,6,6,6}
print(set1)

#Adding item to set
set1.add(10)
print("element added ",set1)

#Union, intersection, difference, symmetric_diference
set2=(1,5,23,56,7)
print("Union of sets: ",set1.union(set2))
print("Intersection of sets: ",set1.intersection(set2))
print("difference of sets: ",set1.difference(set2))
print("symmentric diff of sets: ",set1.symmetric_difference(set2)) 

#ARRAYS
import array as arr
a=arr.array('i',[1,2,3,4,5])

print("array elements are: ")
for nums in a: 
    print(nums)

#adding element
a.append(20)

print("element deleted :",a.pop())"""

