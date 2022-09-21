from LinkedStack import LinkedStack
from LinkedQueue import LinkedQueue

#2개의 스택을 사용하여 큐의 enqueue()와 dequeue() 알고리즘 구현
class TwoQueueStack:
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()


    def __move_elements(self, s, ts):
        while not s.isEmpty():
            ts.push(s.pop())

    def enqueue(self, x):
        self.__s.push(x)

    def dequeue(self):
        self.__move_elements(self.__s, self.__ts)
        return self.__ts.pop()

if __name__ == "__main__":
    que = TwoQueueStack()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())