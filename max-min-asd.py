def swap(k1,adr1,k2,adr2,a,b):
    # a - indeks w tablicy pierwszego el
    adr2[adr1[a]] = b 
    adr2[adr1[b]] = a

    k1[a], k1[b] = k1[b], k1[a]
    adr1[a], adr1[b] = adr1[b], adr1[a]


class Node():
    pass

p = Node() // tutaj p jest wskaznikiem na obiekt!
p.val = 13
p.next = None

//scalanie 2 lancuchow posortowanych rosnaco

def connect(n1,n2):
    out = None
    if n1 == None : return n2
    if n2 == None : return n1

    if n1.val == n2.val :
        out = n2
        n2 = n2.next
    else :
        out = n1
        n1 = n1.next
    last = out
    while n1 != None and n2 != None :
        if n1.val > n2.val :
            last.next = n2
            n2 = n2.next
        else :
            last.next = n1
            n1 = n1.next
        last = last.next
    if n1 == None :
        last.next = n2
    else : 
        last.next = n1
    return out

