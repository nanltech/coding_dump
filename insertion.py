import timeit

def insertionSort(a):
    for i in range(len(a)):
        key=a[i]
        while i>0 and key<a[i-1]:
            a[i]=a[i-1]
            i-=1
        a[i]=key
        print(a)

a=[2,5,7,9,4,7,74,5,1]

start = timeit.default_timer()
insertionSort(a)
stop = timeit.default_timer()
print((stop-start)*1000)

