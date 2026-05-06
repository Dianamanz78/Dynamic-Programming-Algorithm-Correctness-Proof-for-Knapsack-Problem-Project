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
    
W = 3
val = [5, 6, 7]
wt  = [2, 1, 1]

maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 5
val = [15, 16, 4]
wt  = [4, 5, 6]

maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 100
val = [25, 13, 13]
wt  = [75, 50, 50]

maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 10
val = [20, 15, 2]
wt  = [10, 2, 4]

maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)

W = 7
val = [16, 19, 23, 28]
wt  = [2, 3, 4, 5]

maxVal, itemsPicked = greedyKnapsack(W, val, wt)
print("max value: ", maxVal)
print("value of items picked: ", itemsPicked)
