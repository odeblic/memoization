# Regular function
def fibonacci(n):
  return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


# Function with cache
__fib_cache = {}
def fibonacci_c(n):
  if n in __fib_cache:
    return __fib_cache[n]
  else:
    __fib_cache[n] = n if n < 2 else fibonacci_c(n-2) + fibonacci_c(n-1)
    return __fib_cache[n]


# Decorator
def memoize(f):
  cache = {}
  def decorated_function(*args):
    if args in cache:
      return cache[args]
    else:
      cache[args] = f(*args)
      return cache[args]
  return decorated_function


# Function with cache and decorator
@memoize
def fibonacci_cd(n):
  return n if n < 2 else fibonacci_cd(n-2) + fibonacci_cd(n-1)


# Improved decorator
def memoize_i(f):
  cache = {}
  return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]


# Function with cache and improved decorator
@memoize_i
def fibonacci_cdi(n):
  return n if n < 2 else fibonacci_cd(n-2) + fibonacci_cd(n-1)


# Execution of each version of Fibonacci function
for n in range(0, 35):
  print('fibonacci({})\t->\t{}'.format(n, fibonacci(n)))

for n in range(0, 35):
  print('fibonacci_c({})\t->\t{}'.format(n, fibonacci_c(n)))

for n in range(0, 35):
  print('fibonacci_cd({})\t->\t{}'.format(n, fibonacci_cd(n)))

for n in range(0, 35):
  print('fibonacci_cdi({})\t->\t{}'.format(n, fibonacci_cdi(n)))

