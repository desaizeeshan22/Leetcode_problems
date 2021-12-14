def heapify(i,n,array):
    lchild=2*i+1
    rchild=2*i+2
    largest=i
    if (lchild<n) and array[lchild]>array[largest]:
        largest=lchild
    if rchild<n and array[rchild]>array[largest]:
        largest=rchild
    if largest!=i:
        array[i],array[largest]=array[largest],array[i]
        heapify(largest,n,array)
def heap_sort(array):
    n=len(array)
    for i in range(n//2,-1,-1):
        heapify(i,n,array)
    for i in range(n-1,-1,-1):
        array[0],array[i]=array[i],array[0]
        heapify(0,i,array)
    return array

print(heap_sort([12, 11, 13, 5, 6, 7]))