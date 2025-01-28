import time
import math

def simple_prime_algorithm(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

# Test both algorithms with increasing N and compare times
N_values = [1000, 5000, 10000, 20000]
times_simple = []
times_sieve = []

for N in N_values:
    # Simple Algorithm
    start_time = time.time()
    simple_primes = simple_prime_algorithm(N)
    times_simple.append(time.time() - start_time)

    # Sieve of Eratosthenes
    start_time = time.time()
    sieve_primes = sieve_of_eratosthenes(N)
    times_sieve.append(time.time() - start_time)

print("Comparison of time taken for different values of N:")
for i, N in enumerate(N_values):
    print(f"N = {N}")
    print(f"  Simple Algorithm: {times_simple[i]:.6f} seconds")
    print(f"  Sieve of Eratosthenes: {times_sieve[i]:.6f} seconds")
    print(f"  Slowdown factor: {times_simple[i] / times_sieve[i]:.2f}x")
