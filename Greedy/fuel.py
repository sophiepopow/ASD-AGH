def gasoline(D,f):
    counter = 0
    for i in range(len(D)):
        if f < D[i]:
            return None
        n = f
        ds = D[i]
        while n > ds:
            i += 1
            ds += D[i]
        if n < ds:
            i -= 1
        counter += 1
    return counter