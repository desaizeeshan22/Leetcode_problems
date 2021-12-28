def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    # def longest_subs(text1,text2,i,j,memo={}):
    #     if (i,j) in memo:
    #         return memo[(i,j)]
    #     if i==len(text1) or j==len(text2):
    #         return 0
    #     if text1[i]==text2[j]:
    #         memo[(i,j)]=1+longest_subs(text1,text2,i+1,j+1)
    #         return memo[(i,j)]
    #     else:
    #         memo[(i,j)]=max(longest_subs(text1,text2,i+1,j),longest_subs(text1,text2,i,j+1))
    #         return memo[(i,j)]
    # return longest_subs(text1,text2,0,0)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if text1[row - 1] == text1[col - 1]:
                table[row][col] = 1 + table[row - 1][col - 1]
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])
    return table[n][m]

print(longestCommonSubsequence("abcde", "ace"))


