def sum_of_digits(number):
    if number==0:## once the func reaches a single digit then a division by 10 leads to zero as a quotient which is the base case
        return 0
    quotient,remainder=divmod(number,10) ## remainder is obtained by popping off Least significant digit at each iteration
    ## quotient is the remaining portion to operate on
    return sum_of_digits(quotient)+remainder
    
print(sum_of_digits(1214))