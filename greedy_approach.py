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
    
W = 3
val = [5, 6, 7]
wt  = [2, 1, 1]

maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 5
val = [15, 16, 4]
wt  = [4, 5, 6]

maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 100
val = [25, 13, 13]
wt  = [75, 50, 50]

maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 10
val = [20, 15, 2]
wt  = [10, 2, 4]

maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 7
val = [16, 19, 23, 28]
wt  = [2, 3, 4, 5]

maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

