# VARIABLE - nickname for a value
#name = value
score = 0 
item = "bananas"

#LISTS/ARRAYS - a way to store multiple values
grocery_list = ["apples", "pears","cherries", "oreos"] 

#grocery_list
# print(grocery_list[0], "2.99")

# LOOP - a way to repeat code
# FOR EACH - loops around a list
for i in grocery_list:
  print(i, "2.99")
  print("on sale!")

# too add an item
grocery_list.append(item)
grocery_list.append("yogurt")
print(grocery_list)

# remove
grocery_list.pop(0)
grocery_list.pop(4)
grocery_list.remove("oreos")
print(grocery_list)

# for i in grocery_list:
#   print("hi")
#   for i in range(3):
#     print("inside of 3 loop")

# FUNCTIONS: instruction to do an action
def list_num():
  counter = 0
  for i in grocery_list:
    counter += 1
  print(counter)

list_num()

# CONDITIONAL: used for decision making, tests if condition is true

if "apples" in grocery_list:
  print("apple red")
elif "cherries" in grocery_list:
  print("cherry red")
else:
  print("item not in list")

