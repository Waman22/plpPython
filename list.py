my_list = []  #creating an empty list

add= 10 #to insert a new list of numbers into the empty array
add1= 20
add2= 30
add3= 40
my_list.append(add)
my_list.append(add1)
my_list.append(add2)
my_list.append(add3)
my_list.insert(1,15) # inserts the number 15 in the second position

more =[50,60,70]   # creating the array for extending the my list array

my_list.extend(more)  #function for extending the my-list array
my_list.remove(70)

my_list.sort()  # sorting a list in asceding order 
# Sorting in Descending Order
 #sort a in desceding order  my_list.sort(reverse=True) 

print(my_list)

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)