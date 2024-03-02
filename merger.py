def merge(a,b):
    c=[]
    akey,bkey = 0,0
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
    print(c)
    return c

def mergesort(a):
    if len(a)==1:
        return a

    b=mergesort(a[:len(a)//2])
    c=mergesort(a[len(a)//2:])
    return merge(b,c)

a = [2,4,6,8,9,7,5,3,2,4,6,1]
#mergesort(a)



with open('testdata.txt', 'r') as f:
    arr = f.readlines()
    print(arr[2])
    
for i in arr:
    mergesort(i)   