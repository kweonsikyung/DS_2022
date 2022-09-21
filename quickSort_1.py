import os
from quickSort import *

def do_sort(input_file):
    PATH = os.path.dirname(__file__) + "\\" + input_file
    cnt = dict()

    data_file = open(PATH)
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn in cnt:
            cnt[lpn] +=1
        else:
            cnt[lpn] = 1

    A, B = [], []
    for item in cnt:
        A.append(item)
        B.append(cnt[item])

    B= quickSort(B)
    B.reverse()
    for i in range(10):
        for item in cnt:
            if cnt[item] == B[i]:
                print(item, B[i])
                del cnt[item]
                break

do_sort("linkbench_short.trc")