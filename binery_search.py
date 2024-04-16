import time
import numpy as np
import matplotlib.pyplot as plt
def binarysearch(a, low, high, key):
    if low <= high:
        mid = (high + low) // 2
        if a[mid] == key:
            print("Search Successful key found at location:",mid+1)
            return
        elif key < a[mid]:
            binarysearch(a, low, mid-1, k)
        else:
            binarysearch(a, mid + 1, high, k)
    else:
        print("Search UnSuccessful")
a = [13,24,35,46,57,68,79]
print("the array elements are:",a)
k = int(input("enter the key element to search:"))
binarysearch(a, 0, len(a)-1, k)
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel("list length")
plt.ylabel("time complexity")
times=list()
for i in range(1,10):
    start=time.time()
    m=np.random.randint(1000, size=i*1000)
    
    binarysearch(a)
    end=time.time()
    times.append(end-start)
    print("time taken for binarysearch in",i*1000,"elements is", end-start,"s")   

plt.plot(elements,times,label="binary search")
plt.grid()
plt.legend()
plt.show()

            
