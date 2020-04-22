# Algorytm wyznaczania k'tego co do wielkosci elementu w tablicy
# Aby zmiejszyc moliwosc wystapienia przypadku pesymistycznego 
# mozna uzyc funkcji randomizedPartition 

def partition(arr,start,end):

    middle = (start + end)//2
    n = len(arr)

    arr[middle], arr[n-1] = arr[n-1], arr[middle]
    limit = start

    for i in range(start, n-1):
        if arr[i] < arr[n-1]:
            arr[i], arr[limit] = arr[limit], arr[i]
            limit +=1

    arr[limit], arr[n-1] = arr[n-1], arr[limit]

    return limit

def randomizedSelect(arr, start, end, k):

    q = partition(arr,start,end)

    if k == q:
        return arr[q]
    
    if q > k:
        return randomizedSelect(arr,start,q-1,k)
    else:
        return randomizedSelect(arr, q+1, end, k)

arr = [1, 5, 3 ,8, 9 ,0, -2]
print(randomizedSelect(arr,0, len(arr), 3))
