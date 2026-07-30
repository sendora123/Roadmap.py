grocery_list = ["Tomatoes", "Onions", "Spinach", "Bananas", "Milk"]
print("First item:", grocery_list[0])
print("Last three items:", grocery_list[-3:])

grocery_list.append("Garlic")
print("List:", grocery_list)

grocery_list.insert(1, "Bread")
print("New:", grocery_list)

grocery_list.remove("Spinach")
print("Removed:", grocery_list)

purchased_item = grocery_list.pop(2)
print("After pop:", grocery_list)

del grocery_list[0]
print("After delete:", grocery_list)

print("Purchased item:", purchased_item)

grocery_list.clear()

print("Final list:", grocery_list)