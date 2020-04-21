# Mamy daną tablicę A z n liczbami naturalnymi. 
# Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
# czy w tablicy ponad połowa elementów ma jednakową wartość.

def isMoreThanHalfEqual(arr):

    counter = 0

    for i in range(len(arr)):
        if counter == 0:
            candidate = arr[i]
            counter += 1
        elif candidate == arr[i]:
            counter += 1
        else:
            counter -= 1

    if counter == 0:
        return False
    return True

arr1 = [1,2,3,2,2,1]
print(isMoreThanHalfEqual(arr1))
arr2 = [1,2,3,2,2,1,2]
print(isMoreThanHalfEqual(arr2))