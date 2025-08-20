# 2025.08.20
# 04_sequence.py

x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']

# pick Banana

print(x[4])

print(x[x.index('Banana')])

# define range

print(x[x.index('Banana', 0, len(x))])

# include Banana?

print('Banana' in x)