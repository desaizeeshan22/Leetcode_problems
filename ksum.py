def ksum(array,k,target):
    array.sort()
    res=[]
    if not array:
        return res
    avg_value=target//k
    if array[0]>avg_value or array[-1]<avg_value:
        return res
    if k==2:
        return twosum(array,target)
    for i in range(len(array)):
        if i==0 or array[i-1]!=array[i]:
            for subset in ksum(array[i+1:],k-1,target-array[i]):
                res.append([array[i]]+subset)
    return res

def twosum(array,target):
    lo=0
    hi=len(array)-1
    while lo<hi:
        sum_=array[lo]+array[hi]
        if sum_<target or (lo>0 and nums[lo]!=nums[lo-1]):
            lo+=1
        elif sum_>target or (hi<len(array) and nums[hi]!=nums[hi-1]):
            hi-=1
        else:
            res.append([array[lo],array[hi]])
            lo+=1
            hi-=1
    return res