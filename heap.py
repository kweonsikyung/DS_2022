#삽입코드 - 반복문 버전

class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []

    # def insert(self, x):
    #     i = len(self.__A)
    #     self.__A[i] = x
    #     parent = (i-1) // 2
    
    # 16-20 실행코드 X
    # while(1):
    #     if A[i] <= A[parent]:
    #         break
    #     if i==0:
    #         break

        # while i>0 and self.__A[i] > self.__A[parent]:
        #     self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
        #     i=parent
        #     parent = (i-1) //2

#삽입코드 - 재귀버전
    def insert(self, x):
        self.__A.append(x)
        self.percolateUp(len(self.__A)-1)
 
# #스며오르기
    def percolateUp(self, i:int):
        parent = (i-1) //2
        if i>0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.percolateUp(parent)


#원소 삭제 - A[0] 삭제하고, 마지막 원소를 비어있는 루트 위치로 이동
#힙의 특성을 만족하도록 자식 노드 중 큰값과 교환
#리프 노드로 이동하거나 모든 자식보다 값이 크거나 같으면 종료

#삭제 코드
    def deleteMax(self):
        if(not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] =self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None

#스며내리기
    def __percolateDown(self, i:int): #i는 현재 내 원소의 위치
        child = 2*i + 1
        rightChild = 2*i +2
        if (child <= len(self.__A)-1):
            if (rightChild <= len(self.__A)-1 and self.__A[child] < self.__A[rightChild]):
                child = rightChild
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)

    def buildHeap(self):
        for i in range((len(self.__A)-2)//2, -1, -1):
            self.__percolateDown(i)

    def max(self):
        return self.__A[0]

    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A= []

    def size(self) -> int:
        return len(self.__A)

    def headPrint(self):
        height = 0
        n=0
        print("==========================")
        for i in range(len(self.__A)):
            print(self.__A[i], end=' ')
            n+=1
            if n==2**height:
                height +=1
                n=0
                print("\n")
        print("\n")

