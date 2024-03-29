from LinkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, x):
        self.__list.insert(0,x)

    def pop(self):
        return self.__list.pop(0)

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.get(0)

    def isEmpty(self):
        return self.__list.isEmpty()

    def popAll(self):
        self.__list.clear()

    def printStack(self):
        print("Stack from top:", end=' ')
        for i in range(self.__list.size()):
            print(self.__list.get(i), end=' ')
        print()

st1= LinkedStack()
print(st1.top())
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty?', st1.isEmpty())