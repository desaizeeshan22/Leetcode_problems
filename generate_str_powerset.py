subset=set()
subset.add(" ")
input_str="abc"

def gen_subset(input_str,comb=[]):
    if input_str=="":
        return 
    for i in range(len(input_str)):
        comb.append(input_str[i])
        subset.add("".join(comb))
        gen_subset(input_str[i+1:],comb)
        comb.pop()
gen_subset(input_str)
print(subset)