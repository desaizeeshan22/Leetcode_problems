def min_heapify(arr,i,n):
    lchild=2*i+1
    rchild=2*i+2
    smallest=i
    if lchild<n and arr[lchild]<arr[smallest]:
        smallest=lchild
    if rchild<n and arr[rchild]<arr[smallest]:
        smallest=rchild
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        min_heapify(arr,smallest,n)
arr= [25,15,10,40,30,35]

def heap_sort_desc(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        min_heapify(arr,i,n)
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        min_heapify(arr,0,i)
    return arr
print(heap_sort_desc(arr))
