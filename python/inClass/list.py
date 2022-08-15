from ast import Try
from xml.dom.minidom import Element


a = [1, 2, 3, 1, 2 ,3]
b = [4, 5, 6]

# access the elements in a list 
# a[0] = 15
# print(a)

## print a slice of the list
# print(a[0:3]) #a[starting : ending]

# # add to lists
# print(a + b)

# # double the same elements
# print(2*a)

# # to get the index value of a element
# print(a.index(1,3,6)) # index(element, startingIndex, endingIndex)

# # insert a element at the end of the list
# a.append(35)
# print(a)

# # insert a value at a index value
# a.insert(2, 34)   #insert(index, element)
# print(a)

# # remove the item by it's index value
# a.remove(2)
# print(a)

## remove the items
# a.pop(2) # default value is -1
# removed = a.pop() # to store the removed value in another variable
# print(a)


# # make the list empty 
# a.clear()
# print(a)

# # to delete the list entirely
# del(a)

# # count number of elements 
# print(b.count(7))

# # reverse the list
# print(b.reverse)

# # sort in ascending order
# print(b.sort())

# #sort in descending order
# print(b.sort(reverse=True))


# # to copy the list to another variable
# c = b.copy()

# # write a program to print sum of the element of a list without using inbuilt function 
# numbers = [1, 2, 3, 4, 5]
# sumOfNumbers = 0

# for number in numbers:
#     sumOfNumbers += number
# print(sumOfNumbers)


# # write a program to create a list of elements from the keyboard 
# numbers = []
# while True:
#     n = input('enter the number(to stop enter q) : ')
#     if n.lower() == 'q':
#         break
#     else:
#         numbers.append(n)

# print('you entered these values',numbers)


# # write a program to remove the duplicate element from the given list
# l = [15, 2, 14, 15, 7, 14, 15, 36, 2]
# unique = []

# for i in l:
#     if i not in unique:
#         unique.append(i)
    
# print(unique)


# # maximum element from the given list without using inbuilt function
# l = [15, 2, 14, 36, 7, 9]
# max = l[0]

# for element in l:
#     if element > max:
#         max = element
# print(max)


# # minimum element from the given list without using inbuilt function
# l = [15, 2, 14, 36, 7, 9]
# min = l[0]

# for element in l:
#     if element < min:
#         min = element
# print(min)



# sort a list without using the inbuilt methods 













