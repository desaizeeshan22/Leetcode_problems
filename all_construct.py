results=[]
def all_construct(target, word_array,comb=[]):
    if target=="":
        global results
        results+=[comb[:]]
        return
    for word in word_array:
        if target.find(word)==0:
            comb.append(word)
            all_construct(target.replace(word,""),word_array,comb)
            comb.pop()
    return

all_construct("abcdef",["ab","abc","cd","def","abcd","ef","c"])
print(results)