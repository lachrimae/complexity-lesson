def best_max(l):
    result = l[0]
    for entry in l:
        if entry > result:
            result = entry
    return result

maximum_algorithms = [best_max]
fibonacci_algorithms = []