class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        def dp(i, day,memo={}):
            # Base case, it's the last day so we need to finish all the jobs
            state=(i,day)
            if state in memo:
                return memo[state]
            if day == d:
                memo[state]=hardest_job_remaining[i]
                return hardest_job_remaining[i]
            
            best = float("inf")
            hardest = 0
            # Iterate through the options and choose the best
            for j in range(i, n - (d - day)): # Leave at least 1 job per remaining day
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1)) # Recurrence relation
            memo[state]=best
            return  memo[state]
        return dp(0,1)
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        