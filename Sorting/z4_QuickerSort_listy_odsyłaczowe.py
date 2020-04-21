class Node:
    def __init__(self):
        self.next = Null
        self.val  = Null

def partition (L):
   
    pivot = L[0].next

    tmp = Node()
    left = (tmp,tmp)
    tmp = Node()
    right = (tmp,tmp)

    curr = pivot.next
    
    while curr != end :
        if curr.val < pivot.val:
            left[1].next = curr
            left[1] = curr
        else:
            right[1].next = curr
            right[1] = curr
        curr = curr.next
        
    left[1].next = pivot
    pivot.next = right[0].next

    return (left[0].next, right[1], pivot)

def Quicker_sort(L):
   
    (start, end) = L

    #if start == end
    if L[0] == L[1]:
        return

    (left,right,pivot) = partition(L)
        
    start.next = left
    right.next = end

    Quicker_sort((start, pivot))
    Quicker_sort((pivot, end))
