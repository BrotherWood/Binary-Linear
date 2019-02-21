import random
from timeit import default_timer as timer

 
def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = int(l + (r - l)/2)
        if arr[mid] == int(x): 
            return mid 
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1
lim=0
while(lim<7):
    n = input("Masukan Data :")
    arr = [i for i in range(1,int(n)+1)]
    # Test array 
    x = input("Masukan Data Yang Dicari : ")
    start = timer()
    
    result = binarySearch(arr, 0, len(arr)-1, int(x)) 

    if result != -1: 
            print ("Element is present at index %d" % result) 
    else: 
            print ("Element is not present in array")
        
    end = timer()
    
    interval = (end - start)*1000
    print(str(interval) + " milisecond")
    lim=lim+1
