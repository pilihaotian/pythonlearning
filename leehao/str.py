a = ['a', 'c', 'b']
b = a.copy()
a.append('d')
print(a)
print(b)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
