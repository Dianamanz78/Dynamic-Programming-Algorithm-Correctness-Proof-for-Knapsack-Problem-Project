import time
import random
import matplotlib.pyplot as plt

def getPickedItems(W, val, wt, table):
    n = len(val)
    items = []
    while n > 0 and W > 0:
        if wt[n-1] > W:
            n -= 1
            continue

        pick = val[n-1] + table[n-1][W - wt[n-1]]
        notPick = table[n-1][W]

        if pick >= notPick:
            items.append(val[n-1])
            W -= wt[n-1]

        n -= 1
    return items

def DP(W, val, wt):
    # initialize table
    n = len(val)
    # base case: no items or no capacity
    table = [[0] * (W + 1) for _ in range(n + 1)]
    
    # go through row by row
    for i in range(1, n + 1):
        for w in range(W + 1):
            # check if adding the current item does not exceed capacity
            if wt[i-1] <= w:
                # compute value if we pick the item and not pick the item and choose the max
                table[i][w] = max(
                    val[i-1] + table[i-1][w - wt[i-1]],
                    table[i-1][w]
                )
            # if item exceeds capacity, then use value of not picking the item
            else:
                table[i][w] = table[i-1][w]
    
    itemsPicked = getPickedItems(W, val, wt, table)
    return table[n][W], itemsPicked

def greedyKnapsack(W, val, wt):
    # get ratios
    ratios = []
    for x in range(len(val)):
        ratios.append(val[x] / wt[x])
    
    # sort
    sorted_indices = sorted(range(len(val)), key=lambda i: ratios[i], reverse=True)

    currWt = 0
    maxVal = 0
    itemsPicked = []
    
    for i in sorted_indices:
        if currWt + wt[i] <= W:
            currWt = currWt + wt[i]
            maxVal = maxVal + val[i]
            itemsPicked.append(val[i])
        else:
            continue
    
    return maxVal, itemsPicked

# generate random tests
def generate_test(n, max_wt=50, max_val=100):
    val = [random.randint(1, max_val) for _ in range(n)]
    wt = [random.randint(1, max_wt) for _ in range(n)]
    W = 200
    return W, val, wt

def measure(func, W, val, wt, runs=10):
    total = 0
    for _ in range(runs):
        start = time.time()
        func(W, val, wt)
        total += time.time() - start
    return total / runs

size = [50, 100, 200, 400, 800]
greedy_times = []
dp_times = []

for n in size:
    W, val, wt = generate_test(n)

    greedy_times.append(measure(greedyKnapsack, W, val, wt))
    dp_times.append(measure(DP, W, val, wt))

print("size:", size)
print("Greedy times:", greedy_times)
print("DP times:", dp_times)

plt.plot(size, greedy_times, label="Greedy", marker='o')
plt.plot(size, dp_times, label="DP", marker='o')

plt.xlabel("Number of items (n)")
plt.ylabel("Runtime (seconds)")
plt.title("Greedy vs DP Knapsack Runtime")
plt.legend()
plt.grid(True)

plt.show()
