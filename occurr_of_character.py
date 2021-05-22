elem = (input('enter a sentance\n'))
compe = input('character that you want to count occourrence for\n')
total = ''
for i in elem:
    if i == compe:
        total += i
print(len(total))
