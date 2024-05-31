# coding: utf-8
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
    
x =intersect([1, 2, 3, 4], (1, 4))
x
s1 = 'SPAM'
s2 = 'SCAM'
[x for x in s1 if x in s2]
s1 = "SPAM"
s2 = "SCAM"
[x for x in s1 if x in s2]
line = 'aaa,bbb,cccc.dd\n'
line
line.strip()
line
line1 = line.strip()
line1
'%s, eggs, and %s' % ('spam', 'SPAM!')
'{0}, eggs, and {1}' .format('spam', 'SPAM')
'{}, eggs, and {}' .format('spam', 'SPAM')
dir(s1)
help(s1.repalce)
help(s1.replace)
S ='A\nB\tC'
len(S)
S
print(S)
S = 'A\oB\OC'
S = 'A\OB\OC'
S = 'A\0B\0C'
S
print(S)
len(S)
L = [123, 'spam', 1.23]
L[123, 'spam', 1.23]
L= [123, 'spam', 1.23]
type(L)
len(L)
print(L)
L
L[0]
L[::-1]
L[:-1]
L[:]
L[:2]
L + [4, 5, 6]
L + [4, 5, 6] #conctinating a string
L * 2 # concactinating 
L
L.reverse()
L
print(L)
L.reverse()
L
print(L)
L.append('NI')
L
L.pop()
L
L.pop(0)
L
del L[0]
L
print(L)
M = ['bb', 'aa', 'cc']
M.sort()
M
M.reverse()
M
M[99]
M[98] = 1
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
M
type(M)
M[1]
M[1][2]
col2 = [row[1] for row in M]
col2
M
[row[1] + 1 for row in M] 
[row[1] for row in M if row[1] % 2 == 0]
diag = [M[i][i] for i in M [0, 1, 2]]
diag = [M[i][i] for i in [0, 1, 2]]
diag
doubles = [c* 2 for c in 'spam']
doubles
doubles = [c* 2 for c in 'spam']
print(doubles = [c* 2 for c in 'spam'])
print([c* 2 for c in 'spam'])
list(range(4))
list(range(-6, 7, 2))
[[x**2, x** 3] for x in range(4)]
[[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
M
G = (sum(row) for row in M)
next(G)
next(G)
next(G)
list(map(sum, M))
{sum(row) for row in M}
{i : sum (M[i]) for i in range (3)} # creates key/value table of rows
ord('a')
[ord(x) for x in 'spaam'] 
{ord(x) for x in 'spam'}
{x : ord(x) for x in 'spam'}
(ord(x) for x in 'spaam')
D = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink'}  # cratind a dict 
D = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink'}  # cratind a dict
D
D['food'] #fetchinf value of key 'food'
D['quantity'] + 1
D
D['quantity'] +=  1
D
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
D
print(D['name'])
list(D.keys())
D.keys()
D['name']
bob1 = dict(name='Bob', job='dev', age='40')
bob1
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))  #creating dictionary thru zipping method.
bob2
rec = {'name' : {'first': ' Bob', 'last' : 'Smith'}},
rec = {'name' : {'first': ' Bob', 'last' : 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5} 
rec
rec['name']
rec['jobs'] #'jobs' is a nested list
rec['name']['last']  #index the nested dictionary
rec['jobs'][-1] #index the nested list
rec['jobs'].append('janitor')  #Expand Bob's job description
rec['jobs'].append('janitor')  #Expand Bob's job description
rec
