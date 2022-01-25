input_list=["a","a","b","b","c","c","d","d","e","e"]
def length_encoding(input_list):
    i=0
    j=1
    count=1
    if len(input_list)==1 or len(input_list)==0:
        return input_list
    for j in range(1,len(input_list)+1):
        if j<len(input_list) and input_list[j-1]==input_list[j]:
            count+=1
        else:
            input_list[i]=input_list[j-1]
            i+=1
            if count>1:
                for elem in str(count):
                    input_list[i]=elem
                    i+=1
            count=1
    return input_list

print(reverse([1, 3, 8, 4,7,6,5,1]))