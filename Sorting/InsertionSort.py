def insertionSort(arr):
    n = len(arr)

    for i in range(1,n):

        j = i-1
        element = arr[i]
        while j >= 0 and element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = element
        
    return arr

