## Given a target string and an array of words in a word bank,find out if the target
## string can be constructed using the words in the word bank
##function can_construct(target:str,word_array:list) return bool
## using top down recursion and checking if each substring in the array list is a prefix of the remaining substring
## after remove

def can_construct(target, word_array,memo={}):
    if target in memo:
        return memo[target]
    if target=="":
        return True
    for word in word_array:
        if target.find(word)==0:
            res=can_construct(target.replace(word,""),word_array,memo)
            if res:
                memo[target] = True
                return True
    memo[target] = False
    return False

print(can_construct("abcdef",["ab","abc","cd","def","abcd"]))
print(can_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(can_construct("eeeeeeeeeeeeedf",["e","ee","eee","eeee","eeeeee","eeeeeeeeee"]))

