# n - liczba kubełków
def bucketSort(arr, n):
    norm = max(arr)

    # list of n empty lists
    buckets = [[] for _ in range(n)]

    for number in arr:
        normalized_number = number / norm
        bucket_id = int(n* normalized_number)
        buckets[bucket_id].append(number)

    for i in range(n):
        buckets[i] = sorted(buckets[i])

    result = []

    for i in range(n):
        for j in range(len(buckets[i]))
            result.append(buckets[i][j])
    
    return result