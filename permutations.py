output=[]
def backtrack(index,nums):
    if index==len(nums):
            output.append(nums[:])
    for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            backtrack(index+1,nums)
            nums[i],nums[index]=nums[index],nums[i]
            
backtrack(0,[1,2,3])
print(output)