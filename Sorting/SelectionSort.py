def min(start, end, arr):
    res = start
    for i in range(start+1,end):
        if arr[res] > arr[i]:
            res = i
    return res

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        mini = min(i,n,arr)
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

