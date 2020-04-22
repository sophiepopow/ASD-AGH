def heapify(arr, index, size):

    n = len(arr)
    baby1 = 2*index
    baby2 = 2*index+1

    largest = index

    if baby1 < n and arr[baby1] > arr[largest]:
        largest = baby1
    if baby2 < n and arr[baby2] > arr[largest]:
        largest = baby2
    if arr[largest] <= arr[index]:
        return

    arr[largest], arr[index] = arr[index], arr[largest]

    heapify(arr,largest,size)

    return arr

def heapSort(arr):
    n = len(arr)
    for i in range((n//2-1),-1,-1):
        heapify(arr, i, n)
        
    for i in range(n-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


