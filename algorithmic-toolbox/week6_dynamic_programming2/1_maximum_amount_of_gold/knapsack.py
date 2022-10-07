# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    knapsackValues = [[0 for i in range(W + 1)] for y in range(len(w) +1)]
    for i in range(1, len(w) +1):
        currentValue = currentWeight = w[i - 1]
        for c in range(W + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i -1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i -1][c], knapsackValues[i -1][c - currentWeight] + currentValue)
    return knapsackValues[-1][-1]

if __name__ == '__main__':     
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


