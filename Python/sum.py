def count_arrangements(g, y, r, last_ball=None, memo={}):
    # Base case: all balls are placed
    if g == 0 and y == 0 and r == 0:
        return 1

    # Check memoization
    if (g, y, r, last_ball) in memo:
        return memo[(g, y, r, last_ball)]

    total_arrangements = 0

    # Try placing a green ball
    if g > 0 and last_ball != 'G':
        total_arrangements += count_arrangements(g - 1, y, r, 'G', memo)

    # Try placing a yellow ball
    if y > 0 and last_ball != 'Y':
        total_arrangements += count_arrangements(g, y - 1, r, 'Y', memo)

    # Try placing a red ball
    if r > 0 and last_ball != 'R':
        total_arrangements += count_arrangements(g, y, r - 1, 'R', memo)

    # Store result in memo
    memo[(g, y, r, last_ball)] = total_arrangements
    return total_arrangements


# Input values
g = 1
y = 1
r = 1

# Calculate arrangements
result = count_arrangements(g, y, r)
print("Output:", result)
