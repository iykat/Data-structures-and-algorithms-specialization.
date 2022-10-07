def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    while left <= right:
        pivot = (left + right) // 2
        if keys[pivot] < query:
            left = pivot + 1
        elif keys[pivot] > query:
            right = pivot - 1
        else:                                             
            if pivot - 1 < 0:
                return pivot
            if keys[pivot - 1] != query:
                return pivot
            right = pivot - 1
    return -1

# [-14, -10, 2, 108, 108, 243, 285, 285, 401], 108

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
