##Given a string containing digits from 2-9 inclusive,
##return all possible letter combinations that the number could represent. Return the answer in any order.

#A mapping of digit to letters (just like on the telephone buttons) is given below.
#Note that 1 does not map to any letters.

#2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    results = []
    hash_map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    def backtrack(combination, index):
        if index == len(digits):
            results.append("".join(combination))
            return
        letters = hash_map[int(digits[index])]
        for letter in letters:
            combination.append(letter)
            backtrack(combination, index + 1)
            combination.pop()

    backtrack([], 0)
    return results