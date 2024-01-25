def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2

    x = 2
    y = 2
    d = 1

    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def smallest_prime_factor(n):
    if n < 2:
        return None  # No prime factors for numbers less than 2
    result = pollards_rho(n)
    
    # If the result is not a prime factor, we need to find the smallest prime factor
    while result != n and result is not None:
        temp_result = pollards_rho(result)
        if temp_result is not None:
            result = temp_result
        else:
            break

    return result

# Example usage:
number = int(input("Enter a number: "))
result = smallest_prime_factor(number)

if result is None:
    print(f"{number} has no prime factors.")
else:
    print(f"The smallest prime factor of {number} is: {result}")

