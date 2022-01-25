import plotly.express as px
import pandas
import random
import worksheet
import sys
import math
import timeit

def random_list(length):
    result = list()
    for i in range(length):
        result.append(random.random())
    return result

def plot_algorithms(df):
    fig = px.line(df.sort_values(by="input_size"), x="input_size", y="avg_duration", color="algorithm")
    fig.show()

if __name__ == '__main__':
    if sys.argv[1] == 'max':
        algorithms = worksheet.maximum_algorithms
        for algorithm in algorithms:
            assert algorithm([1, 2, 3, 4, 5]) == 5
            assert algorithm([1, 2, 3, 3, 2]) == 3
    elif sys.argv[1] == 'fib':
        algorithms = worksheet.fibonacci_algorithms
        for algorithm in algorithms:
            assert algorithm(7) == 13
    else:
        sys.exit(1)

    df = pandas.DataFrame({
        'input_size': [],
        'avg_duration': [],
        'algorithm': [],
    })
    for algorithm in algorithms:
        if sys.argv[1] == 'max':
            length_range = range(1, int(sys.argv[2]))
            number_of_iterations = 100
        elif sys.argv[1] == 'fib':
            # exponential: stop around 33
            # logarithmic: stop around 1200
            length_range = range(int(sys.argv[2]))
            number_of_iterations = 3
        for input_length in length_range:
            total_time = 0
            for i in range(number_of_iterations):
                if sys.argv[1] == 'max':
                    r_list = random_list(input_length)
                    total_time += timeit.timeit(lambda: algorithm(r_list), number=1)
                elif sys.argv[1] == 'fib':
                    total_time += timeit.timeit(lambda: algorithm(input_length), number=1)
            average_time = total_time / number_of_iterations
            df = df.append(pandas.DataFrame({
                'input_size': [input_length],
                'avg_duration': [average_time],
                'algorithm': [algorithm.__name__]
            }), ignore_index=True)
    print(df)
    plot_algorithms(df)