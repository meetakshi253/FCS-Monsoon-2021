''' The Diffie-Hellman Algorithm
Meetakshi Setiya, 2019253
'''

import gmpy2
from gmpy2 import mpz

rand_state = gmpy2.random_state(hash(gmpy2.random_state()))

def bob_sends_alice(p, g):
    '''
    Input: Takes a prime number p and large number q upto 1023 digits long.
    Generates a random number b having at least 1000 digits.
    Computes the public exchange B.
    Return: a tuple of B and b.
    '''
    lower_bound = mpz(10**(999))
    upper_bound = mpz((10**1023))
    b = gmpy2.add(lower_bound, gmpy2.mpz_random(rand_state, upper_bound))  #a random number with 1000 to 1024 digits
    B = gmpy2.powmod(g, b, p)
    print("\nB: ", B)
    print("b: ", b)
    return (B, b)

def alice_sends_bob(p, g):
    '''
    Input: Takes a prime number p and large number q upto 1023 digits long.
    Generates a random number a having at least 1000 digits.
    Computes the public exchange A.
    Return: a tuple of A and a.
    '''
    lower_bound = mpz(10**(999))
    upper_bound = mpz((10**1023))
    a = gmpy2.add(lower_bound, gmpy2.mpz_random(rand_state, upper_bound))   #a random number with 1000 to 1024 digits
    A = gmpy2.powmod(g, a, p)
    print("\nA: ", A)
    print("a: ", a)
    return (A, a)

def print_shared_secret_alice(B, a, p):
    '''
    Input: Takes in Bob's public exchange key B, Alice's secret integer a, and p.
    Computes the shared secret.
    '''
    shared_secret = gmpy2.powmod(B, a, p)
    print("\nShared secret (Alice): ", shared_secret)
    return

def print_shared_secret_bob(A, b, p):
    '''
    Input: Takes in Alice's public exchange key A, Bob's secret integer b, and p.
    Computes the shared secret.
    '''
    shared_secret = gmpy2.powmod(A, b, p)
    print("\nShared secret (Bob): ", shared_secret)
    return

def main():
    p = mpz(input("p (prime number): ")) #a large enough prime number else it is highly likely to have same public exchange keys because of the `mod p` in the algorithm.
    g = mpz(input("g : "))
    B, b = bob_sends_alice(p,g)
    A, a = alice_sends_bob(p,g)
    print_shared_secret_alice(B, a, p)
    print_shared_secret_bob(A, b, p)
    return

main()
 
 