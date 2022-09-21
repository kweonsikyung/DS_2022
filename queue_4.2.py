from LinkedStack import LinkedStack
from LinkedQueue import LinkedQueue
#2개의 큐를 사용하여 스택의 push()와 pop() 알고리즘 구현
class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()


    def __move_elements(self, q, tq):
        while not q.isEmpty():
            tq.enqueue(q.dequeue())

    def push(self, x):
        self.__q.enqueue(x)
        # self.__move_elements(self.__tq, self.__q)

    #size를 쓰는 방법 // q가 isEmpty 일때는 enqueue를 하지 않는 방법
    def pop(self):
        while self.__q.size()==1:
            self.__move_elements(self.__q, self.__tq)
            ret = self.__q.dequeue()
        self.__move_elements(self.__tq, self.__q)
        return ret
        
if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())