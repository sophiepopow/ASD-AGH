def insert(heap, el):
	arr = heap[0]
	arr.append(el)
	
	i = heap[1]-1
	heap[1] += 1

	while i > 0 and arr[i] > arr[i//2-1]:
		arr[i], arr[i//2-1] = arr[i//2-1], arr[i]
		i = i//2-1

def get_max/min(heap):
	# heap = (arr, size)
	arr = heap[0]

	res = arr[0]
	arr[0] = arr[n-1]
	heap[1] -= 1
	heapify(heap[0],0, heap[1])
	return res


def peek(arr):
#sprawdzenie wartości bez usuwania z kopca
	return arr[0]
