# basic list:
"""
a = [1,2,3,5]
b =["color","red","yelllow","green"]
c =[]
print(a)
print(b)
print(c)
"""

# index concepts:
"""
marks = [90,78,66,43]
marks[0] = 20
marks[-1] = 70
print(marks)
"""

# nested list:
"""
my_list = ["welcome",3.12,50,[10,20,30]]
my_list.append(10)
my_list.extend([40,50,60])
print(my_list)
"""

# built in function concepts:
"""
a = [1,2.5,30,99]
print(len(a))
print(max(a))
print(min(a))
a.append(40)
print(a)

b = [1,2,3,4]
b.extend([4,5,6,])
print(b)

c = [2,7,1,8,5,9,9]
d = c.copy()
d.pop()
print(d)

e = [1,1,1,2,2,3,4,5,]
print(e.count(1))

f = [1,2,3,4,5,6]
f.remove(1)
print(f)

g = [1,2,5,4,3,8]
g.insert(0,"ram")
print(g)

h = [1,3,9,5,2,8,7]
h.sort()
print(h)
h.sort(reverse=True)
print(h)
"""

#list some concepts: 
"""
Marks = [60,70,50,30]
print(Marks[0])
print(Marks[-1])
money = [10,20,30,40,70,50]
i = 0
while i<len(money):
    print(money[i])
    i+=1
"""

#reverse indexing:
"""
money = [10,20,30,40,50]
i = -1
while i>=(-len(money)):
    print(money[i])
    i-=1
"""

#list len() concepts:
"""
a = [10,20,30,40,50]
print(len(a))

b = ["tamil","english","maths","science","social"]
c=b
i = 0
while i<len(b):
    print(b[i])
    i+=1

d=c
for i in c:
    print(i)
"""

#singl value change concepts:
"""
num1 = [2,4,5,8,10]
print("Elements before update:")
for i in num1:
    print(i)
num1[2] = 6
print("Elements after updates:")
for i in num1:
    print(i)
"""
#continues value change concepts:
"""
num2 = [1,2,3,4,5]
print("Elements before update:")
for x in num2:
    print(x)
num2[0:5] = 6,7,8,9,10
print("Elements after update:")
for x in num2:
    print(x)
"""

# first 10 natural numbers n**2 concepts:
"""
squre = []
for i in range(1,11):
    s = i**2
    squre.append(s)
print(squre)
"""

#list comprehensions concepts:
"""
squre = [i**2 for i in range(1,11)]
print(squre)
"""

# 1 to 20 natural numbers divide by 4 concepts:
"""
div4 = []
for i in range(1,21):
    if i%4==0:
        div4.append(i)
print(div4)
"""

#list member ,not member concepts:
"""
country = ["india","russia","america","london","japan"]
member = input("enter your countey:")
if member in country:
    print(member,"is the member of the world")
else:
    print(member,"is not member of the world")
"""
