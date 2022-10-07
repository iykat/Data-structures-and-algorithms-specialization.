# Uses python3
def edit_distance(s, t):
    #write your code here. i am writing
    cache = [[float("inf")] * (len(t) + 1) for i in range(len(s) + 1)]
    
    #filling in the base case
    for i in range(len(t) + 1):                    # filling the last row
        cache[len(s)][i] = len(t) - i 
    for j in range(len(s) + 1):                    # filling the last column
        cache[j][len(t)] = len(s) - j 
           
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) -1, -1, -1):
            if s[i] == t[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
    return cache[0][0]
 
# s = 'editing'
# t = 'editing'
# print(edit_distance(s, t))    

if __name__ == "__main__":
    print(edit_distance(input(), input()))
