def knapsack(W, val, wt, n, table):
    # base case: no items or no capacity
    if n == 0 or W == 0:
        table[n][W] = 0
        return 0
    
    # if subproblem has been done before
    if table[n][W] != -1:
        return table[n][W]
    
    # compute value if we pick the item
    pick = 0
    if wt[n-1] <= W:
        pick = val[n-1] + knapsack(W - wt[n-1], val, wt, n-1, table)
    
    # compute value not picking the item
    notPick = knapsack(W, val, wt, n-1, table)
    
    table[n][W] = max(pick, notPick)
    return table[n][W]

def getPickedItems(W, val, wt, table):
    n = len(val)
    items = []
    while n > 0 and W > 0:
        if table[n][W] != table[n-1][W]:
            items.append(val[n-1])
            W = W - wt[n-1]
        n = n -1 
    return items

def DP(W, val, wt):
    n = len(val)
    
    #initialize table with -1 for memoization
    table = [[-1] * (W + 1) for _ in range(n+1)]
    
    # compute max value
    for i in range(n + 1):
        for w in range(W + 1):
            knapsack(w, val, wt, i, table)
    maxVal = table[n][W]
    
    # get list of items chosen
    itemsPicked = getPickedItems(W, val, wt, table)
    
    return maxVal, itemsPicked
    
W = 4
val = [1, 2, 3, 5]
wt = [4, 5, 1, 2]
maxVal, itemsPicked = DP(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)
