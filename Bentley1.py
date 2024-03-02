# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def merge(a,b):
    c=[]
    akey,bkey=0,0
    while akey<len(a) and bkey<len(b):
        if a[akey]<b[bkey]:
            c.append(a[akey])
            akey+=1
        else:
            c.append(b[bkey])
            bkey+=1
    if akey==len(a):
        c.extend(b[bkey:])
    else:
        c.extend(a[akey:])
    return c

def mergesort(a):
    if len(a)==1:
        return a 
    
    b=mergesort(a[:len(a)//2])
    c=mergesort(a[len(a)//2:])
    return merge(b,c)

def solution(A):
    arr = mergesort(A)

    if arr[len(arr)-1]<0:
        return 1
    elif arr[0]<1:
        return 1
    else:

        for i in range(len(arr)-1):
            if arr[i]>0:
                if arr[i]+1 != arr[i+1] and arr[i]!=arr[i+1]:
                    return arr[i]+1
        return arr[len(arr)-1]+1
