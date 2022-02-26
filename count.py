def print_count(arr):
    for i in range(len(arr)):
        flag=False
        for j in range(0,i):
            if arr[i]==arr[j]:
                flag=True
                break
        if flag==True:
            continue
        freq=1
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                    freq+=1
        print(arr[i],freq)
print_count([10,20,20,30,10])