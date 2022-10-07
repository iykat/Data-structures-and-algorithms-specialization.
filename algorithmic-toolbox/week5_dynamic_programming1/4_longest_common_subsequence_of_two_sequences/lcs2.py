#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                
    
    return dp[0][0]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

# a = [1, 3, 4, 5, 6]
# b = [1, 2, 4, 5, 6]

# print(lcs2(a,b))