def decode_message(s: str, p: str) -> bool:
    m, k = len(s), len(p)
    
    # DP table with dimensions (m+1) x (k+1)
    dp = [[False] * (k + 1) for _ in range(m + 1)]
    
    # Base case: empty message matches with empty pattern
    dp[0][0] = True
    
    # Handle cases where pattern starts with '*' (can match empty string)
    for j in range(1, k + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]  # Match single character
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]  # Match zero or more characters
    
    return dp[m][k]