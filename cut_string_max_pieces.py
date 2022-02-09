## n= string length , a,b,c allowable piece size
## cut the string into allowable chunks from the set above so that it forms max number of pieces
# return -1 if not possible to cut the string into allowable sizes
result=-1
def max_pieces(n,p_sizes,num_pieces=0):
    if n==0:
       global result
       result=max(result,num_pieces)
       return
    if n<0:
        return
    for size in p_sizes:
        num_pieces+=1
        max_pieces(n-size,p_sizes,num_pieces)
        num_pieces -=1
    return

# max_pieces(5,[2,5,1])
max_pieces(23,[12,9,11])
print(result)