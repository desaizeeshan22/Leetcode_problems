## Given a 2D grid find the number of ways to go from the top-left to the bottom right of the grid
## the only movements allowed are down or right

def grid_traveller(m,n,memo={}):
    '''input :takes in m rows and n columns of the input 2D array
    m:int ,n:int 
    output:int returns the number of ways to go from top left to bottom right
    '''
    ## recursive strategy with memoization
    if (m,n) in memo:
        return memo[(m,n)]
        
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    value=grid_traveller(m-1,n,memo)+grid_traveller(m,n-1,memo)
    memo[(m,n)]=value
    return value
print(grid_traveller(1,1))
print(grid_traveller(2,2))
print(grid_traveller(2,3))
print(grid_traveller(3,3))