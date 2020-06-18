# 2020-06-18
# Выдача суммы

coins = [1, 2, 5, 9, 10, 25, 50]
cache = {}


def bills(sum):
    if sum in coins:
        return [sum]

    if sum in cache.keys():
        return cache[sum]

    ways = {}
    for coin in reversed(coins):
        if coin <= sum:
            ways[coin] = bills(sum - coin)

    coin = None
    for coin1 in ways.keys():
        if coin is None or len(ways[coin1]) < len(ways[coin]):
            coin = coin1

    cache[sum] = [coin] + ways[coin]
    return [coin] + ways[coin]


for s in range(1, 100):
    print(s, bills(s))
