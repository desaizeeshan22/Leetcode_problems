def how_sum(target,input_arr):
    table=[None for _ in range(target+1)]
    table[0]=[]
    for i in range(len(table)):
        for elem in input_arr:
            if (i+elem)<=target and table[i] is not None:
                table_elem_copy=table[i].copy()
                table_elem_copy.append(elem)
                table[i+elem]=table_elem_copy
    return table[target]


print(how_sum(7,[5,3,4]))

