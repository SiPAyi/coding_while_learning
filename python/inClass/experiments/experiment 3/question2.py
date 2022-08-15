# Write a program to create a list of words and print the longest word from the list?

L = ['sai', 'sravan', 'srinadh', 'shreyash', 'manikanta', 'praneel', 'ranga', 'vamshi']
longest = L[0]

for name in L:
    if len(name) > len(longest):
        longest = name
    
print(longest)
