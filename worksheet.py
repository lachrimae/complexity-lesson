list1 = [1,3,7,11,41,3]

def find_max(list1):
    max = None
    for i in list1:
        if max is None:
            max = i
        if max < i:
            max = i
    return max

def bad_max(list1):
  for i in list1:
    larger_than_the_rest = True
    for j in list1:
      if j > i:
        larger_than_the_rest = False
    if larger_than_the_rest:
      return i
  return None

maximum_algorithms = [find_max, bad_max, max]

# The Fibonacci sequence is defined as follows:
#   F_0 = 0
#   F_1 = 1
# for n greater than 1, 
#   F_n = F_(n-1) + F_(n-2)
def fibonacci(n):
    # return ?

fibonacci_algorithms = []

if __name__ == '__main__':
    find_max(list1)
