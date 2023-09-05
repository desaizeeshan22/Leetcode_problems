class Solution {
    public int coinChange(int[] coins, int amount) {
        return dp(coins,amount,new HashMap<>());
        
    }
     public int dp(int[] coins, int amount, Map<Integer, Integer> cache) {
        if (cache.containsKey(amount)) {
            return cache.get(amount);
        }
        if (amount == 0) {
            return 0;
        }
        if (amount < 0) {
            return -1;
        }
        int result = Integer.MAX_VALUE;
        for (int coin : coins) {
            int minCalls =  dp(coins, amount - coin, cache);
            if (minCalls >= 0) {
                result = Math.min(result,1+ minCalls);
            }
        }
        if (result != Integer.MAX_VALUE) {
            cache.put(amount, result);
        } else {
            cache.put(amount, -1);
        }
        return cache.get(amount);
    }
}