def afunct(alist):
    #This if statement is to check if the input is a list
    if type(alist) != list:
        raise TypeError("This is not a list")
    #This for loop is to iterate through the list and count up the positive ints
    for int in alist:
        positive_int = 0
        if int > 0:
            positive_int += 1
            return positive_int

afunct([1, 5, -5, 6, -2, 4, -10, 7])
afunct("This is a string")
