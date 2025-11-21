# # PRACTICE QUESTIONS
# 1. create a list of 5 fruits and print the second item
fruits = ["apple","banana","grapes","watermelon","oranges"]
print(fruits[1] ) # output is mango
# 2.replace the third item in the list with "mango"
fruits[2] = "mango"
print (fruits)
# 3. add "grapes" to the list
fruits.append("grapes")   # output  ['apple', 'banana', 'mango', 'watermelon', 'oranges', 'grapes']
print(fruits)
# 4.remove the first item in the list
fruits.pop(0)
print(fruits)   #output is ["banana","mango","watermelon","oranges","grapes"]
# 5 use a loop to print all the items in the list
for item in fruits:
    print(item)   # output is banana
# mango
# watermelon
# oranges
# grapes
    
 # 6 create a list of numbers  and find its length.
numbers =[1,2,3,4,5,6,7,8,9]
print(len(numbers))  #output s9