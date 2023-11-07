# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity W 


def knapSack(W, wt, val, n): 

	# Base Case 
	if n == 0 or W == 0: 
		return 0

	# If weight of the nth item is 
	# more than Knapsack of capacity W, 
	# then this item cannot be included 
	# in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
			knapSack(W, wt, val, n-1)) 

# end of function knapSack 


# Driver Code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	print (knapSack(W, weight, profit, n)) 


#using dynamic programming
# Python code to implement the above approach 


def knapSack(W, wt, val, n): 
	
	# Making the dp array 
	dp = [0 for i in range(W+1)] 

	# Taking first i elements 
	for i in range(1, n+1): 
		
		# Starting from back, 
		# so that we also have data of 
		# previous computation when taking i-1 items 
		for w in range(W, 0, -1): 
			if wt[i-1] <= w: 
				
				# Finding the maximum value 
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1]) 
	
	# Returning the maximum value of knapsack 
	return dp[W] 


# Driver code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	print(knapSack(W, weight, profit, n)) 



