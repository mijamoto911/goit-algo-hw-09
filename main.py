import timeit

def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    coins_count = {}

    for coin in denominations:
        count = amount // coin
        coins_count[coin] = count

        amount -= count * coin

    return coins_count

amount = 113
result = find_coins_greedy(amount)

greedy_time = timeit.timeit("find_coins_greedy(100)", globals=globals(), number=1000)

print(result)
print(f"Execution time of the greedy algorithm: {greedy_time} сек.")


def dynamic_find_coins(amount):
    denominations = [50, 25, 10, 5, 2, 1]

    min_coins_count = [float('inf')] * (amount + 1)
    min_coins_count[0] = 0

    last_coin_used = [-1] * (amount + 1)

    for coin in denominations:
        for i in range(coin, amount + 1):
            if min_coins_count[i - coin] + 1 < min_coins_count[i]:
                min_coins_count[i] = min_coins_count[i - coin] + 1
                last_coin_used[i] = coin

    min_coins = min_coins_count[amount]

    coins_used = {}
    while amount > 0:
        coin = last_coin_used[amount]
        if coin not in coins_used:
            coins_used[coin] = 1
        else:
            coins_used[coin] += 1
        amount -= coin

    return coins_used

amount = 113
result = dynamic_find_coins(amount)
dynamic_pr_time = timeit.timeit("dynamic_find_coins(100)", globals=globals(), number=1000)

print(result)
print(f"Execution time of the dynamic programming algorithm: {dynamic_pr_time} сек.")

