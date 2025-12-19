def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount %= coin
            result[coin] = count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Ініціалізуємо таблицю мінімальної кількості монет для кожної суми до target
    # Використовуємо float('inf'), щоб позначити недосяжні суми на початку
    min_coins = [0] + [float('inf')] * amount
    # Зберігаємо останню додану монету, щоб відтворити результат
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Відтворюємо склад монет зі словника
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
        
    return result

# Приклад тестування
test_amount = 113
print(f"Жадібний алгоритм для {test_amount}: {find_coins_greedy(test_amount)}")
print(f"Динамічне програмування для {test_amount}: {find_min_coins(test_amount)}")