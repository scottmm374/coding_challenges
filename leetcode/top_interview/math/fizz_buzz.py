def fizzBuzz(n):
        
        fizzy_buzz = []
        
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizzy_buzz.append("FizzBuzz")
                continue
            elif num % 3 == 0:
                fizzy_buzz.append("Fizz")
            elif num % 5 == 0:
                fizzy_buzz.append("Buzz")
                
            else:
                fizzy_buzz.append(str(num))
                
        return fizzy_buzz


# Runtime: 57 ms  beats 59.11%
# Memory Usage: 14.9 MB beats 88.55 %