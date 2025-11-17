#Class 3


#Set




#Dictionary
def phonebook():
    my_dict = {}
    user_input = input("Enter choice: ").lower()
    while user_input != "exit":
        if user_input == "add":
            name = input("Enter name to add: ")
            number = input("Enter number to add: ")
            my_dict[name] = number
        elif user_input == 'find':
            name = input("Enter name you want to find: ")
            print(my_dict[name])

        elif user_input == "remove":
            name = input("Enter name you want to remove: ")
            my_dict.pop(name)
        user_input = input("Enter choice: ").lower()
    print(my_dict)
# phonebook()






def shopping():
    shopping_cart = {"milk": 10, "water": 3, "tank": 2000000}
    for val in shopping_cart.values():
        print(val)

# shopping()
















def two_list_to_dict(first_list, second_list):
    final_dict = {}
    for i in range(len(first_list)):
        final_dict[first_list[i]] = second_list[i]



list1 = [1,2,3,4,5]
list2 = ["Hello", "How", "Are", "You", "Goodbye"]

two_list_to_dict(list1,list2)







def merge_dict(first_dict, second_dict):
    final_dict = {}

    for item in first_dict.items():
        final_dict[item[0]] = item[1]

    for item in second_dict.items():
        final_dict[item[0]] = item[1]

    for item in final_dict.items():
        print(item)



dict1= {"key1": 1, "key2":2, "key3":"hello"}
dict2= {"key4": 4, "key5":5, "key6":"goodbye"}

# merge_dict(dict1, dict2)









#Tuple
def tuple_one(tup):
    product = 1
    for num in tup:
        product *= num

    length_tup = len(tup)
    print(product)
    print(product ** (1/length_tup))



my_tuple = (4,5,3,3,4,7,6)
# tuple_one(my_tuple)






