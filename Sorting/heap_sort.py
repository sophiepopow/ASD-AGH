def heapify(arr, index, size):

    n = len(arr)
    baby1 = 2*index
    baby2 = 2*index+1

    largest = index

    if baby1 < n and arr[baby1] > arr[largest]:
        largest = baby1
    if baby2 < n and arr[baby2] > arr[largest]:
        largest = baby2
    if array[largest] <= array[index]:
        return

    arr[largest], arr[index] = arr[index], arr[largest]

    heapify(arr,largest,size)

    return arr

