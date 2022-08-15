height = int(input('enter height : '))

for k in range(height):
    previousRowsLastTerm = int(k*(k+1)*0.5)
    text = ''
    for i in range(k+1):
        text += str(i + previousRowsLastTerm + 1) + ' '
    print(text)
