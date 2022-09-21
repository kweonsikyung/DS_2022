def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last) #가장 큰 수 A[k] 찾기
        A[k], A[last] = A[last], A[k] #교환 스와이프

def theLargest(A, last:int) -> int: #가장 큰 수의 인덱스 리턴하기
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
    return largest
