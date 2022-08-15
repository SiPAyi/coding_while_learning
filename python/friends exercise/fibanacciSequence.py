sequence = [0,1]

nthTerm = int(input('enter how many terms do you want : '))

for i in range(nthTerm-2):
    sequence.append(sequence[i] + sequence[i+1])

print(sequence[:nthTerm])


