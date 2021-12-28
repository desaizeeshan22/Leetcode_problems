class Solution(object):
    def coinChange(self, coins, amount):
        def coin_change(coins,amount,memo={}):
            if amount in memo:
                return memo[amount]
            if amount<0:
                return -1
            if amount==0:
                return 0
            min_=float("inf")
            for coin in coins:
                res=coin_change(coins,amount-coin,memo)
                if res>=0:
                    min_=min(min_,1+res)
            memo[amount]=min_ if min_!=float("inf") else -1   
            return memo[amount]
        return coin_change(coins,amount)
            
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        