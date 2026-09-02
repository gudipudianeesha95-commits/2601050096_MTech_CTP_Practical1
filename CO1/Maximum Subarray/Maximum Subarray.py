# Maximum Subarray - Daily Life Example
# Example: Finding the maximum profit earned over consecutive days

def max_subarray(profits):
    max_current = profits[0]
    max_global = profits[0]

    for i in range(1, len(profits)):
        max_current = max(profits[i], max_current + profits[i])

        if max_current > max_global:
            max_global = max_current

    return max_global


# Daily profit/loss for a shop
profits = [100, -50, 200, -100, 300, -50, 150]

maximum_profit = max_subarray(profits)

print("Daily profits/losses:", profits)
print("Maximum profit from consecutive days:", maximum_profit)