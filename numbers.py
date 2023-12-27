
import math

def generate_primes(bound):
    primes = [2] # Begin with the first prime
    yield 2
    for potential in range(2, bound):
        sq_potential = math.sqrt(potential)
        #print("Assessing potential {}, sqrt is {}".format(potential, sq_potential))
        #print("Primes: {}".format(primes))
        # Try all primes up until the square root
        # of potential. If none of them evenly divide
        # potential, then it is in fact a prime
        for prime in primes:
            # Not a prime; move on
            if potential % prime == 0:
                #print("  Prime {} divides potential {}".format(prime, potential))
                break
            # Got past sqrt(potential)! It is a prime!
            if prime > sq_potential:
                #print("  Because prime {} > sqrt {}: Potential {} is prime!".format(
                    #prime,
                    #sq_potential,
                    #potential
                #))
                primes.append(potential)
                yield potential
                break


