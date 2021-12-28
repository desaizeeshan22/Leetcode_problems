def coin_change(coins, amount, memo={}):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    min_ = float("inf")
    for coin in coins:
        res = coin_change(coins, amount - coin, memo)
        if res >= 0:
            min_ = min(min_, 1 + res)
    memo[amount] = min_
    return -1 if memo[amount]==float("inf") else memo[amount]


print(coin_change([1,2,5],11))
print(coin_change([2],3))

