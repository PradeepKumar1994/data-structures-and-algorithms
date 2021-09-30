
def heapify(arr,n, i):

    max = i
    left = (2*max)+ 1
    right = (2*max)+2

    if(left < n and arr[max] < arr[left]):
        max = left

    if(right < n and arr[max] < arr[right]):
        max = right

    if(i != max):
        arr[max], arr[i] = arr[i], arr[max]
        heapify(arr, n, max)

    #return arr
        

def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1,0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr= heapify(arr, i, 0)

    #return arr



arr = [12, 11, 13, 5, 6, 7]
print(heapsort(arr))
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),
