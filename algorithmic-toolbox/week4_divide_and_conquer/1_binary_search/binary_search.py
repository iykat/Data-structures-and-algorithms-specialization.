def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    while left <= right:
        pivot = (left + right) // 2
        if keys[pivot] < query:
            left = pivot + 1
        elif keys[pivot] > query:
            right = pivot - 1
        else:
            return pivot 
    return -1


if __name__ == '__main__':
    num_keys = int(input()) 
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
