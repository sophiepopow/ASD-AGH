def merge_sort(arr,start,end):
    if end - start == 1:
        return
    middle = (start + end)//2

    merge_sort(arr,start,middle)
    merge_sort(arr,middle,end)

    tmp1 = arr[start:middle]
    tmp2 = arr[middle:end]

    index = start
    i = 0
    j = 0

    while i<len(tmp1) and j<len(tmp2) :
        if tmp1[i] < tmp2[j] :
            arr[index] = tmp1[i]
            i+=1
            index+=1
        else:
            arr[index] = tmp2[j]
            j+=1
            index+=1
        
    while i<len(tmp1) :
        arr[index] = tmp1[i]
        i+=1
        index+=1
    while j<len(tmp2) :
        arr[index] = tmp2[j]
        j+=1
        index+=1