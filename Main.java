import java.util.HashMap;
import java.util.Map;

public class Main
{
  public Main()
  {
    Map<Integer, Integer> cache = new HashMap<>();
  }

  private Map<Integer, Integer> cache;

  public Integer fibonacci(Integer n)
  {
    if(cache.containsKey(n))
    {
      return cache.get(n);
    }
    else
    {
      Integer result;
      if(n < 2)
      {
        result = 1;
      }
      else
      {
        result = fibonacci(n-2) + fibonacci(n-1);
      }
      cache.put(n, result);
      return result;
    }
  }

  public static void main(String[] args)
  {
    Main main = new Main();
    
    for(int n = 0; n <= 40; ++n)
    {
      System.out.println("fibonacci(" + n + ")\t->\t" + main.fibonacci(n));
    }
  }
}

