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

W = 4
val = [1, 2, 3, 5]
wt = [4, 5, 1, 2]
maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("items picked: ", itemsPicked)
