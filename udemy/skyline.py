def myfunc(inpt):
    test_list1 = []
    i = ""
    for x, y in enumerate(inpt):
        if x%2 != 0:
            i = y.upper()
            test_list1.append(i)
        if x%2 == 0:
            i = y.lower()
            test_list1.append(i)
    return ''.join(test_list1)
