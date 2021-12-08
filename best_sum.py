def best_sum(target_sum,numbers,memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum<0:
        return None
    if target_sum==0:
        return []
    shortest_combo=None
    for elem in numbers:
        remainder=target_sum-elem
        res=best_sum(remainder,numbers,memo)
        if res is not None:
            res.append(elem)
            if shortest_combo is None or len(res)<len(shortest_combo):
                     shortest_combo=res
    memo[target_sum] = shortest_combo
    return shortest_combo

print(best_sum(7,[5,4,3,7]))
print(best_sum(8,[2,3,5]))
print(best_sum(8,[2,3,5]))