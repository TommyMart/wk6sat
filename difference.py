num1 = 5 # assign 5 to num1

num2 = num1 # assigned the value to num1 to 2

num1 = 10 # changed the value of num1 to 10

print(num1)
print(num2)

list1 = [1, 2, 3, 4] # assign [] to list1

list2 = list1 #assign list1 to list2 # copy by address (or reference / not a new list)

list1.append(5) # change something in list1

print(list1)
print(list2)

list3 = list1.copy() # copy
