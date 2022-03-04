#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        def reverse(arr,i,j):
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        #Your code here
        A.reverse()
        D=D%N
        reverse(A,0,N-D-1)
        reverse(A,N-D,N-1)
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends