# Uses python3
import sys

def get_change(m):
    #write your code here
    min_coins = 0
    while m >= 10:
        min_coins += 1
        m = m - 10
    while m >= 5:
        min_coins += 1
        m = m - 5
    while m >= 1:
        min_coins += 1
        m = m - 1
    return min_coins

#if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

print(get_change(2009))
