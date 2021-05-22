elem = (input('enter the elements of list separated by space:- ').split(' '))
com = int(input('enter the number against you want to compare this element of list:- '))
ints = [int(item) for item in elem]
test = []
for i in ints:
    if i < com:
        test.append('sm')
    else:
        test.append('bg')
for i in test:
    if i == 'bg':
        print("list have element whcih is => than compair value")
        exit()
else:
    print('all element of list is smaller than compare input')
