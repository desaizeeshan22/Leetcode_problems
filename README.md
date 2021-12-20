DP(Bottom up approach)
#Tabulation recipe(Used for bottom up approach aka use the smaller subproblems iteratively to build up the
main problem from the bottom to the top


1)Visualize the problem as a table


2)Size the table based on the inputs


3)Initialize the table with default values


4)Seed the trivial answer to the table aka the base case in case of fibonacci f(0),f(1) aka 0,1 respectively


5)Iterate through the table


6)Fill the further postitions used on current position


DP(Top down)(break the main problems into subproblems by calling the function recursively from the main problem to the
sub problems at every recursive call till you reach the base case or trivial case)
(use memoization to optimize the brute force strategy):


1)Make it work(Use brute force for correctness)

    Visualize the problem as a tree
    
    
    Implement the tree using recursion
    
    
    leaves of the trees are the base cases or trivial cases
    
    Test brute force solution
2)Make it efficient

    Use a memo object (store the key as the function arguments and value as the result in the memo object before returning the
result)


    Add a base case to return memo values aka if the arguments are already in the memo object use the value to return result
