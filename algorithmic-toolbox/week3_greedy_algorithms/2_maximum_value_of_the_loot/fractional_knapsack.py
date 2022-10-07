# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unit_values = [values[i]/weights[i] for i in range(len(values))]
    for i in range (len(values)):
        if capacity == 0:
            return value
        else:
            max_value_index = unit_values.index(max(unit_values)) 
            max_weight = weights[max_value_index]
            a = min(max_weight, capacity) 
            value += a * unit_values[max_value_index]
            capacity -= a
            weights[max_value_index] -= a
            
            unit_values[max_value_index] = 0
             
    return value 
            
            

    


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
