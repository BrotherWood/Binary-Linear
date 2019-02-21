import random
from timeit import default_timer as timer
 
def sequensialSearch (arr, key): 
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

z=1
while z<8:
    n = input("Masukan Data :")
    data = [i for i in range(1,int(n)+1)]
    random.shuffle(data)

# Test array

    
    x = input("Masukan Data Yang Dicari : ")

    start = timer()
    result = sequensialSearch(data, int(x)) 
    end = timer()

    if result != -1: 
            print ("Element is present at index %d" % result) 
    else: 
            print ("Element is not present in array")
    interval=(end-start)*1000
    print(str(interval)+" milisecond ")
    z=z+1
