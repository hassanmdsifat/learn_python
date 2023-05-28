with open('test_file.txt', 'a') as file:
    my_list = ["This is item 1\n", "This is item 2\n", "This is item 3\n"]
    file.write("This is from our program test\n")
    file.writelines(my_list)