def can_sum(target,input_arr):
    table=[False]*(target+1)
    table[0]=True
    for i in range(len(table)):
        for elem in input_arr:
            if i+elem<len(table) and table[i]==True:
                table[i+elem]=table[i]
    return table[len(table)-1]

print(can_sum(7,[5,3,4]))
print(can_sum(7,[5,3,4,7]))
print(can_sum(7,[2,4]))
print(can_sum(300,[7,14]))

