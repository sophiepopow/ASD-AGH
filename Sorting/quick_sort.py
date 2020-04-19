def divide(arr,start,end):
    middle = (start + end)//2
    n = len(arr)

    arr[middle], arr[n-1] = arr[n-1], arr[middle]
    limit = start

    for i in range(start, n-1):
        if arr[i] < arr[n-1]:
            arr[i], arr[limit] = arr[limit], arr[i]
            limit +=1

    arr[limit], arr[n-1] = arr[n-1], arr[limit]

    return limes

def quick_sort(arr, start, end):

    if end - start <= 1:
        return

    middle = divide(arr,start,end)
    quick_sort(arr, start, middle)
    quick_sort(arr, middle+1, end)

    return arr