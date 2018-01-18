INSTRUCTIONS = """
Your quirky boss collects rare, old coins...

They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.

Example:

For amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢),
your program would output 4—the number of ways to make 4¢ with those denominations

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
"""

def solution(inputs):
    amount, denominations = inputs
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += \
                ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]

test_case_inputs = [
    [4, [1,2,3]]
]
