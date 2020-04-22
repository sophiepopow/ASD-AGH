def countingSort(arr):
    n = len(arr)
    k = max(arr)

    count = [0]*k
    result = [0]*n

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1,k):
        count[i] += count[i-1]

    for i in range(n,-1,-1):
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return result