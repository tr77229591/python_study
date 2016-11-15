from time import time
import pickle

print(time())

class Calculator:
    def __init__ (self,name='old name',price=199,height=300):
        self.name=name
        self.price=price
        self.height=height
    
    def add(self,x,y):
        self.name='new name'
        result = x+y
        print(result)
        print(self.name)
        return result
    def minus(self,x,y):
        print(self.name)
        result=x-y
        return result
    




aa=input('give us a input')
print('the input is ',aa)



d={'apple':1,'pear':2}

print(d['pear'])



dic={'da':111,'23':2}
file=open('pickle.pickle','wb')
pickle.dump(dic,file)
