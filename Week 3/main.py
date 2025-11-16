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

shopping()












dict1= {"key1": 1, "key2":2, "key3":"hello"}

