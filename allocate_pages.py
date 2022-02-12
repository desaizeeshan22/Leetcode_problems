# Given an array of integers A of size N and an integer B.
#
# College library has N bags,the ith book has A[i] number of pages.
#
# You have to allocate books to B number of students so that
# maximum number of pages alloted to a student is minimum.
#
# A book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example:
# A student cannot be allocated book 1 and book 3, skipping book 2.
# Calculate and return that minimum possible number.

# NOTE: Return -1 if a valid assignment is not possible.
def allocate(arr,k):
    if len(arr)==1:
        return arr[0]
    if k==1:
        return sum(arr)
    res=-1
    for i in range(1,len(arr)):
        res=min(res,max(sum(arr[:i]),allocate(arr[i:],k-1)))
    return res
arr=[12,34,67,90]
k=2
def is_possible(arr,threshold,k):
    student_allocated=1 ## initially zero pages assigned and starting from 1 student minimum
    pages=0
    for i in range(len(arr)):
        if arr[i]>threshold:
            return False
        if (arr[i]+pages)>threshold:
            student_allocated+=1
            pages=arr[i]
        else:
            pages+=arr[i]

    return False if student_allocated>k else True
def optimized(arr,k):
    lo=max(arr) ## if every book is assigned to one student each value becomes the num pages of the
                # book itself so the  the num pages here is the max value of array as that is the only max
                ##available
    hi=sum(arr) ## if all the books are assigned to one student then the pages assigned is the sum
                # of all pages
    res=-1
    while lo<=hi:
        mid=(lo+hi)//2 ## the threshold of max pages assigned to each student
        if is_possible(arr,mid,k):## if the threshold enables a possible distribution of pages among
                                    # k student then try to minimize it further
            res=mid
            hi=mid-1
        else:
            lo=mid+1
    return res

##complexity N*logN (N for the is possible as travels the entire array and
# the binary search takes logN time)
print(optimized(arr,k))