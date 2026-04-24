# Dynamic Programming Algorithm Correctness Proof for the Knapsack Problem Project
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
			 if w[i] <= j:
                 # take new item if max
				 A[i][j] = max(A[i][j], v[i] + A[i-1, j – w[i]])	
			 else:
                 # don't take new item
				 A[i][j] = A[i - 1][j]	
```
        
## Greedy Approach

## Proof
Proof. We are proving by induction that for all n and C, K(n, C) will return the maximum value that can be achievable using the first n items and the capacity C.

Theorem:
For all integers $n\geq 0$, and capacity C where $C \geq 0$, K(n, C) will return the maximum value achievable using subset A, where $A \subseteq \{1, ..., n\}$ will hold a set of items such that the total weight is at most C.

Base case: 
if n = 0, then K(0, C) = 0, for all $n\geq 0$
if C = 0, then K(n, 0) = 0, for all $n\geq 0$

Inductive Hypothesis: K(n – 1, C`) is true for all C`$\leq C$

Inductive Step:
Case 1: item n is not included
This means $A \subseteq \{1, ..., n-1\}$
We assume A is an optimal solution
$A_{weight} <= C$
Therefore, A is a valid solution to the subproblem of K(n-1, C)
$A_{value} <= K(n-1, C)$

Case 2:  item n is included
$A=A'∪ \{n\} $ where $A'⊆ \{1, …, n−1\} $
We assume A is an optimal solution 
$Aweight <= C$
$A_{weight} = A'_{weight} + w_n$
Therefore, $A'_{weight} <= C -w_n $
Thus, A` is a valid solution to the subproblem K(n-1, C - wn)
$A'_{value} <= K(n-1, C - w_n)$
$A_{value} <= K(n-1, C - w_n) + v_n$

$A_{value} <= K(n-1, C)$
$A_{value} <= K(n-1, C - w_n) + v_n$
$A_{value} <= max(K(n-1, C), K(n-1, C - w_n) + v_n))$

Conclusion: Thus, by induction we have that the recurrence of K(n, C) = max(K(n-1, C), K(n-1, C - wn) + vn)) is correct in computing the max value for all n and C

## Running the Project


