#include <iostream>
#include <map>


template <typename T, typename U>
T function(T n)
{
  static std::map<T, U> cache;

  if(n <= 1)
  {
    return 1;
  }
  else if(cache.find(n) != cache.end())
  {
    return cache[n];
  }
  else
  {
    unsigned long result = algo(n);
    cache[n] = result;
    return result;
  }
}


unsigned long fibonacci(unsigned long n)
{
  static std::map<unsigned long, unsigned long> cache;

  if(n <= 1)
  {
    return 1;
  }
  else if(cache.find(n) != cache.end())
  {
    return cache[n];
  }
  else
  {
    unsigned long result = fibonacci(n - 1) + fibonacci(n - 2);
    cache[n] = result;
    return result;
  }
}


unsigned long factorial(unsigned long n)
{
  static std::map<unsigned long, unsigned long> cache;

  if(n <= 1)
  {
    return 1;
  }
  else if(cache.find(n) != cache.end())
  {
    return cache[n];
  }
  else
  {
    unsigned long result = n * factorial(n - 1);
    cache[n] = result;
    return result;
  }
}


int main()
{
  for(unsigned long n = 0; n <= 20; ++n)
  {
    std::cout << "factorial(" << n << ")\t->\t" << factorial(n) << std::endl;
  }

  for(unsigned long n = 0; n <= 40; ++n)
  {
    std::cout << "fibonacci(" << n << ")\t->\t" << fibonacci(n) << std::endl;
  }
}

