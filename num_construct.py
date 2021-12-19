## Given a target string and an array of words in a word bank,find out the number of ways the target
## string can be constructed using the words in the word bank
##function can_construct(target:str,word_array:list) return bool
## using top down recursion and checking if each substring in the array list is a prefix of the remaining substring
## after remove


def num_construct(target, word_array,memo={}):
    res=0
    if target=="":
        res=1
        memo[target]=res
        return res
    for word in word_array:
        if target.find(word)==0:
            res+=num_construct(target.replace(word,""),word_array)
    memo[target] = res
    return res

print(num_construct("abcdef",["ab","abc","cd","def","abcd"]))

print(num_construct("purple",["purp","p","ur","le","purpl"]))
print(num_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
num_construct("eeeeeeeeeeeeedf",["e","ee","eee","eeee","eeeeee","eeeeeeeeee"])
