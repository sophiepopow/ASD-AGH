from math import log2

def build_heap(h):
    for i in reversed(range(1, len(h)//2)):
        push_down(h,i)
    return h

def push_down(h,i):
    if(floor(log2(i))%2==0):
        push_down_min(h,i)
    else
        push_down_max(h,i)

def push_down_min(h,i):
    if(i*2<len(h)):
        m = list(
            sorted(
                map(
                    lambda y:(y,h[y]),
                    filter(
                        lambda x:x<len(h),
                        [i*2,i*2+1,i*4,i*4+1,i*4+2,i*4+3]
                    )
                ),
            key=lambda x:x[1])
        )[0][0]
        if m>i*2+1 :
            if h[m]<h[i] :
                h[m], h[i] = h[i], h[m]
                if h[m] >h[m//2]:
                    h[m],h[m//2] = h[m//2],h[m]
                push_down_min(h,m) 
        elif h[m]<[i]:
            h[m], h[i] = h[i], h[m]
            
def push_down_max(h,i):
    if(i*2<len(h)):
        m = list(
            sorted(
                map(
                    lambda y:(y,h[y]),
                    filter(
                        lambda x:x<len(h),
                        [i*2,i*2+1,i*4,i*4+1,i*4+2,i*4+3]
                    )
                ),
            key=lambda x:x[1],reverse=True)
        )[0][0]
        if m>i*2+1 :
            if h[m]>h[i] :
                h[m], h[i] = h[i], h[m]
                if h[m] <h[m//2]:
                    h[m],h[m//2] = h[m//2],h[m]
                push_down_max(h,m) 
        elif h[m]>[i]:
            h[m], h[i] = h[i], h[m]
            
def push_up(h,i):
    if i == 1:
        if floor(log2(i))%2==0 :
            if h[i] > h[i//2]:
                h[i],h[i//2] =h[i//2],h[i]
                push_up_max(h,i//2)
            else:
                push_up_min(h,i)
        else:
            if h[i]< h[i//2]:
                h[i],h[i//2] = h[i//2],h[i]
                push_up_min(h,i//2)
            else:
                push_up_max(h,i)

def push_up_min(h,i):
    if i>3 and h[i]< h[i//4]:
        h[i],h[i//4] = h[i//4],h[i]
        push_up_min(h,i//4)

def push_up_max(h,i):
    if i>3 and h[i] > h[i//4]:
        h[i],h[i//4] = h[i//4],h[i]
        push_up_min(h,i//4)
