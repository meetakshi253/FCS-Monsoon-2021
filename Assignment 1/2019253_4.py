''' RSA Algorithm
Meetakshi Setiya, 2019253
'''

import gmpy2
from gmpy2 import mpz

def validatekeys(e, phi):
    ''' Input: e and the totient phi
    Helper function to check if e and the generated d are different and if d is coprime to phi.
    Return: the tuple (e,d,flag) if they it passes the validation where e and d are a usable component of the key pair, flag=0 if e and d are not equal and 1 if e and d are equal.
    -1 is returned otherwise
    '''
    try:
        d = gmpy2.invert(e,phi)
        if(gmpy2.gcd(d, phi)!=1):
            raise Exception
    
        else:
            if(d!=e):
                return (e, d, 0)
            else:
                return (e,d,1)
    except:
        return -1


def generatekeys(phi):
    ''' Input: the euler's totient phi for p and q
    Generates e and d to be used in the public and private keys respectively.
    Finds the most suitable fermat prime number that can function as e.
    Calculates d by finding the modular multiplicative inverse of d with respect to phi which is also coprime to phi.
    The odds that none of the fermat primes make a suitable e are very low.
    The probability that a prime number e and comparitively larger prime number p have gcd(e, p-1) = 1 are (e-2)/(e-1)
    Return: the tuple (e,d)
    '''
    e=0 
    d=0
    if(phi>65537):
        k = validatekeys(65537, phi)
        if(k!=-1):
            e,d,flag = k
            if(flag==0):
                return (e,d)
    
    if(phi>257):
        k = validatekeys(257, phi)
        if(k!=-1):
            e,d,flag = k
            if(flag==0):
                return (e,d)

    if(phi>17):
        k = validatekeys(17, phi)
        if(k!=-1):
            e,d,flag = k
            if(flag==0):
                return (e,d)
    
    if(phi>5):
        k = validatekeys(5, phi)
        if(k!=-1):
            e,d,flag = k
            if(flag==0):
                return (e,d)

    if(phi>3):
        k = validatekeys(3, phi)
        if(k!=-1):
            e,d,flag = k
            if(flag==0):
                return (e,d)
    
    return (e, d)


def encryptmessage(m, e, n):
    ''' Input: message m, e and n
    Actual encrytption formula applied here
    Return: the encrypted message c
    '''
    c = gmpy2.powmod(m, e, n)
    return c

def encrypt(p, q, m):
    ''' Input: prime numbers upto 1023 digit long p, q and the message m.
    Prints the encoded message (c) along with e, d and n.
    Note that for small values of p and q, e and d may be the same. This is not correct, but was not removed for the sake of maintaining continuity. 
    '''
    n = gmpy2.mul(p,q)
    phi = gmpy2.mul(gmpy2.sub(p,1), gmpy2.sub(q,1))

    if(phi<5):
        print("p and q are too small")
        exit(1)
        
    e, d = generatekeys(phi)   
    c = encryptmessage(m, e, n)
    print("\nc: ", c)
    print("e: ", e)
    print("d: ", d)
    print("n: ", n)
    return

def decrypt(c, d, n):
    ''' Input: encrypted message (c), d and n.
    Prints the decrypted message m.
    '''
    m = gmpy2.powmod(c, d, n)
    print("\nm: ", m)
    return

def main():
    choice = input("Enter 1 for RSA encryption and 2 for RSA decryption: ")
    if(choice == "1"):
        print("note: RSA uses modulo operation so m must not greatly exceed p*q. rsa works best for large p and q")
        p = mpz(input("p (upto 1023 digits): "))
        q = mpz(input("q (upto 1023 digits): "))
        m = mpz(input("m (upto 1023 digits): "))
        encrypt(p, q, m)
    
    elif(choice == "2"):
        c = mpz(input("c: "))
        d = mpz(input("d: "))
        n = mpz(input("n: "))
        decrypt(c, d, n)

    else:
        print("Wrong choice")

main()
