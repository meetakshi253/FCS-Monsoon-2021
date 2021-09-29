''' Meetakshi Setiya, 2019253
'''

import time
import gmpy2
from gmpy2 import mpz

otps = []
rand_state = gmpy2.random_state(hash(gmpy2.random_state()))

def generate():
    ''' Generates and returns a 1023 digit random number. 
    '''
    lower_bound = mpz(10**(1022))
    upper_bound = mpz((10**1023)-1)
    range = gmpy2.add(gmpy2.sub(upper_bound, lower_bound), mpz(1))
    dig1023 = gmpy2.add(lower_bound, gmpy2.mpz_random(rand_state, range))
    return(dig1023)

def otp():
    ''' Populates otps[] list with 100 unique 6-digit OTPs extracted from a single 1023 digit random number.
    (If 100 unique OTPs cannot be generated from a single random number, a new random number is chosen).
    Returns 0 if 100 unique OTPs have been generated, 1 otherwise. 
    '''
    n = str(generate()).strip()
    for i in range(len(n)-5):
        otp6 = n[i:i+6]
        if not (otp6 in otps) and len(otp6)==6:
            otps.append(otp6)
            print(otp6)
            if(len(otps)==100):
                return 0

    for i in range(len(n)-5):    #if somehow the random int doesnt give 100 unique OTPs, extract rest of the OTPs after reversing the integer
        otp6 = n[i+6:i:-1]
        if not (otp6 in otps) and len(otp6)==6:
            otps.append(otp6)
            print(otp6)
            if(len(otps)==100):
                return 0

    return 1

def main():
    while(1):
        if(otp()==0):
            break

start = time.time()
main()
print("\n\n------------- "+ str(time.time() - start)+ " seconds --------------")
print("Time taken to generate 100 OTPs by 2a: 0.26s approx. and by 2b: 0.09s approx.")