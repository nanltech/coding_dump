def root(i):
    return i
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

def heapify(a,i):

    max=a[root(i)]
    print(a,' ',i,' ',max,  ' ',)
    if left(i)<len(a) and a[left(i)]>a[root(i)]:
        max=a[left(i)]
    if right(i)<len(a) and a[right(i)]>max:
        max=a[right(i)]
    print(max)
    if max != root(i) and max==a[left(i)]:
        print('hello')
        a[root(i)],a[left(i)] = a[left(i)],a[root(i)]
        print(left(left(i)), len(a))
        if left(left(i))<len(a):
            heapify(a,i)
    if max!= root(i) and max==a[right(i)]:
        a[root(i)],a[right(i)] = a[right(i)],a[root(i)]
        if left(right(i))<len(a):
            heapify(a,i)

    

def heapsort(a):
    for i in range(len(a)//2-1,-1,-1):
        heapify(a,i)
    print(a)

a = [2,4,6,8,5,3,2,6,4,8,1]
print(a)
heapsort(a)
print(a)


