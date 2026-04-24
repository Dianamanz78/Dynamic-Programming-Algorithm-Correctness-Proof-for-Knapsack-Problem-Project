# Dynamic-Programming-Algorithm-Correctness-Proof-for-Knapsack-Problem-Project
This project is on the correctness proof for a Dynamic Porgramming Algorithm solution for the Knapsack Problem. It will include an implementation of both the Greedy approach and Dynamic Programming approach for the I/O knapsack problem including an analyzation of these two algorithms using multiple test cases and why the DP is the better approach. It will also include the correctness proof of the DP algorithm after establishing that DP is the only option. 

## Author
Diana Manzanes

## Dynamic Programming Approach

```
def Knapsack( W, val, wt, n):
	 # create the table by initializing by 0
	 for i=0 to n:
         # base case: when item is 0, then value is 0
		 A[i][0] = 0 	
	 for j=0 to n:
         # base case: when capacity is 0, then value is 0
		 A[0][j] = 0
    
	 for i to n:
		 for j = 1 to m:
			 \indent \indent \indent if w[i] <= j:
                 \indent \indent \indent \indent \# take new item if max
				 \indent \indent \indent \indent A[i][j] = max(A[i][j], v[i] + A[i-1, j – w[i]])	
			 \indent \indent \indent else:
                 \indent \indent \indent \indent \# don't take new item
				 \indent \indent \indent \indent A[i][j] = A[i - 1][j]	
```
        
## Greedy Approach

## Running the Project


