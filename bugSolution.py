def function_with_uncommon_error_solution(n):
    memo = {}
    def helper(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = helper(n - 1) + helper(n - 2)
            memo[n] = result
            return result
    return helper(n)

result = function_with_uncommon_error_solution(35) # Example that works correctly