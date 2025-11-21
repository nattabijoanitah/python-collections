# # # PYTHON COLLECTIONS
# # # there are mainly four types of python collections namely;
               #LISTS
# lists - are ordered collection of item and can help us do duplicate items and use these brackets [],
# # tuples - are aslo ordered but we cant change them,add,and remove anything, and use these brackets;()
# # set - are unordered and cannot have duplicate members and use these brackets {}
# # dictionary -are ordered ,changeable,but cant have duplicate members because of the unique key value pairs it uses and uses these brackets {}
# examples on lists
names=["joan","goshen","raidah","kimo","nattly","becky"]
print(names)
# list methods 
# 1. the length method , helps us get the number of items in the list.
print(len(names))
print(type(names))
# list indexing(positive and negative indexing);
# accessing list names
print(names[0])   # zero idexing-its the first element
print(names[1])   # zero indexing-its second element in the list
print(names[-1])   # its the last element in the list
print(names[-2])   # its the second_last element in the list
print(names[1:4])  # its from the second to the fourth
print(names[2:])   # returns upto to end of the list
print(names[2:4])   #doesnot return the last element of the list
# List_constructor
mylist = []
mylist = list ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
print(mylist)
print(mylist[1])
print(mylist[0])
print(mylist[-1])  # negative indexing
# changing lists
mylist[5] = "red"
print(mylist)
mylist[-1] = "goshen"
print(mylist)
mylist[1:4] = ["uganda","kenya","japan","china","america"]
print(mylist)
# adding(appending)elements in the list -adds elements at the end
numbers = [10,20,30,40,50]
numbers.append(60)
print(numbers)
# inserting an element - adds at a specific position
numbers.insert(0,90)
print(numbers)
# removing a certain element in the list we use the remove method 
numbers.remove(30)
print(numbers)
# removing all the elements in the list we use the clear method
numbers.clear()
print(numbers)
# exending in a list or merging 
fruits = ["oranges","apple","melon"]
numbers= [1,2,3]
fruits.extend(numbers)
print(fruits)
# removing the last item in the list we use the pop method
numbers= [1,2,3]
numbers.pop()
print(numbers)
# checking for the existance of a number in a list we use the index method
numbers = [1,2,3]
numbers.index(3)
print(numbers)
# looping through a list
fruits = ["oranges","apple","melon"]
for item in fruits:
 print(item)
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.sort() # arranges them in asscending order
print(numbers)
numbers.reverse() #arranges the list in descending order
print(numbers)


