# https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=11
# https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1


class Solution:
    def minDifference(self, arr):
        total_sum = sum(arr)
        n = len(arr)
        target = total_sum // 2  # We only need to consider subset sums up to total_sum/2
        memo = {}

        # Recursive function with memoization
        def solve(i, s1):
            if i == n:
                return abs(total_sum - 2 * s1)  # Calculate min difference
            if (i, s1) in memo:
                return memo[(i, s1)]
            
            # Option 1: Include arr[i] in subset s1 (if within limits)
            include = solve(i + 1, s1 + arr[i]) if s1 + arr[i] <= target else float("inf")
            
            # Option 2: Exclude arr[i] from subset s1
            exclude = solve(i + 1, s1)

            # Store result in memo table
            memo[(i, s1)] = min(include, exclude)
            return memo[(i, s1)]

        return solve(0, 0)




class Solution:
    def minDifference(self, arr, n):
        # code here
        # code for subset sum => for finding last row => possible subsets
        totalsum = sum(arr)
        dp = [[0]*(totalsum + 1) for i in range(n + 1)]
        # 1st row of dp = False; as for arr of size 0 no subsert is possible
        for j in range(totalsum + 1):
            dp[0][j] = False
        # 1st column of dp = Ture; as for target = 0 is possible for empty arr
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, totalsum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Making an array to store possible subset sums
        # from the last row of dp = True
        subsetSums = []
        for j in range(totalsum + 1):
            if dp[n][j] == True:
                subsetSums.append(j)
        #print(subsetSums)
        # s1 + s2 = totalsum
        # s2 = totalsum - s1
        # => s2 - s1 == totalsum - 2 * s1
        mn = float("inf") # minimum Difference of two subset sums
        i = 0
        while 2 * subsetSums[i] <= totalsum:
            mn = min(mn, totalsum - 2 * subsetSums[i])
            i += 1
        
        return mn            
            
            
            
