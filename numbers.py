
import math

"""
Generate a list of the first N prime numbers using a simple memoization scheme.

Said list can be bounded by the number of primes to generate (nth_prime),
or by the maximum value to check for primality (max_value).

We must have max_value OR nth_prime (either or both).
In the case of both bounds being given, the stop condition exorsised
can be chosen to be when EITHER are met, or when BOTH are met.

We simply iterate through the integers, and check if each is prime.
In order to do so, we look for factors of the potential.
That is, if we find a number such that their remainder after division is 0.

Terms
-----
* The Potential: The number under question as to its primality.
* Possible Factors: It is checked whether this number is in fact a factor of
  the Potential in question. This is done using the modulous operator.

In order to cut down on possible factors to check, we shall employ the following:
    1. We already have the list of primes less than this potential.
      We need only check if any of these evenly divide the potential, not all composites.
      (If composite c=pq divides n, then so shall p and q)
    2. It is only necessary to check up to the square root of the potential.
      Any factors greater than the square root will have a corresponding co-factor
      less than the square root.

Leaving us with a rough time complexity to find the nth prime of O(n*sqrt(n))
Tradeoff is that we use O(n) space along the way.

Question:
    The relationship between the value of primes and the number of primes.
    Asked more clearly, distance between primes as we move higher,
    and the ratio of the number of primes found to the number of numbers checked.
    Both of which can change as we move to higher numbers.
"""
def generate_primes(bound):
    primes = [2] # Begin with the first prime
    for potential in range(2, bound):
        # Relatively quick floating-point calculation for later comparison.
        sq_potential = math.sqrt(potential)
        # Try all primes up until the square root of potential.
        # If none of them evenly divide potential, then it is in fact a prime.
        for prime in primes:
            # Not a prime; move on
            if potential % prime == 0:
                break
            # Got past sqrt(potential)! It is a prime!
            if prime > sq_potential:
                primes.append(potential)
                break
    return primes


