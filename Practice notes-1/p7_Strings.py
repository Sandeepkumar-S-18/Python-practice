# String :- A string is a data type in Python, composed of a collection of characters. For example: 'Sandeep','Benakanahalli'
# 1 for single coats
a='sandeepkumar'
print(a)
# output: sandeepkumar

# 2 for double coats
b="sandeepkumar."
print(b)
# output: sandeepkumar.

# 3
c="Tin's birthday"
print(c)
# output: Tin's birthday

# 4
d='Tim said ,"I am busy today".'
print(d)
# output: Tim said ,"I am busy today".

# 5
e='Tim said ,"I\'m busy today".'
print(e,'\n')
# ouput: Tim said ,"I'm busy today".

# 6
f = '''hey there!
welcome to Bangaluru'''
print(f)
# output: hey there!
#         welcome to Bangaluru

# 7 len function
g = 'sandeepkumar'
print(len(g))
# output: 12

# 8 when put the space b/t then it is also count in the lenght
h = 'sandeep kumar'
print(len(h))
# output: 13

# 9
print(h[6],'\n')
# output: p

# 10 every new character in single line
stg='sandeepkumar'
for i in stg:
    print(i)
# output:s
# a
# n
# d
# e
# e
# p
# k
# u
# m
# a
# r

# 11 for print the all character in a single line
stg = 'sandeepkumar'
for i in stg:
    print(i,end='')
# output: sandeepkumar

print('\n')

# 12 slicing
stg = 'sandeepkumar'
print(stg[0:7])
print(stg[:7])
print(stg[7:])
print(stg[2:5])
# output: sandeep
#         sandeep
#         kumar
#         nde

# 13 inbuilt methods
stg = 'Welcome to Bengaluru.'
print(stg.upper())
print(stg.lower())
print(stg.find('B'))
print(stg.index('B'))
print(stg.split(' '))
print(stg.replace('Bengaluru','Karnataka'))
print(stg.rpartition(' to '))  # convert string to tuple
# output: WELCOME TO BENGALURU.
#         welcome to bengaluru.
#         11
#         11
#         ['Welcome', 'to', 'Bengaluru.']
#         Welcome to Karnataka.
#         ('Welcome', ' to ', 'Bengaluru.')

# 14 concatenation
stg1 = 'good'
stg2 = 'morning'
print(stg1+' '+stg2)

stg1 = 'Hey'
stg2 = 'there'
stg3 = 'all'
stg='{} {}, {}!'.format(stg1,stg2,stg3)
print(stg)
# output: good morning
#         Hey there, all!