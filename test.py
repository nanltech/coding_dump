import random
import os
import peak



def func(x, haiyue = "verysmellypoopy"):
    #print(haiyue)
    pass
    
func("x")

#print("hello")
#func("hello") 
def hai():
    a = [1,2,3]
    b = {1,2,3}
    c = "1,2,3"
    d = (1,2,3)
    e = {"name" : "hai" ,"smells" : "bad"}

    print(a,b,c,d,e["name"],e["smells"])
    print("hai is smelly")

a = [1,2,3]
b = [1,2,3]

bounds = (0,0,5,5)
(startRow, startCol, numRow, numCol) = bounds
#print(type((startRow, startCol, numRow, numCol)))

class haiyue:
    
    def __init__(self, smellLevel, stinkyLevel):

        self.smellLevel = smellLevel
        self.stinkyLevel = stinkyLevel

    def testfunc(self):
        print(self.smellLevel, self.stinkyLevel)
    
    def testfunc2(self,x):
        print(self.smellLevel, self.stinkyLevel, x)

f = haiyue(1,"jjj")
f.testfunc2("beige")

p = 9
if p is None: print("oh no")

variable = "problemMatrix"
namespace = dict()
with open("problem.py") as handle:
    exec(handle.read(), namespace)
#print(namespace[variable])

from math import *
#exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})

# object can have squareRoot() module
exec('print("hello")')

answer = []
list1 = [1,2,3,4,5]
list2 = [1]
for a in list1:
    for b in list2:
        answer.append ((a, b))
print(answer)

print([(a, b) for a in list1 for b in list2]) 

def recur(a):

    if a==0: 
        print('you did it')
        return True
    else:
        a = a - 1
        print(a)
        recur(a)


print(recur(0)) 

def anyfunc(a):
    return a+2

print(anyfunc(2))

