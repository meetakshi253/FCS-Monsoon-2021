''' Meetakshi Setiya, 2019253
'''

import time
import gmpy2
from gmpy2 import mpz

rand_state = gmpy2.random_state(hash(gmpy2.random_state()))

def generate():
    ''' Generates a 1023 digit random number; the probability that two generated numbers are equal is very low. 
    Also generates a random index between 0 and 1000 for the extraction of otp.
    Returns a tuple of 1023 digit random number and index.
    '''
    lower_bound = mpz(10**(1022))
    upper_bound = mpz((10**1023)-1)
    range = gmpy2.add(gmpy2.sub(upper_bound, lower_bound), mpz(1))
    dig1023 = gmpy2.add(lower_bound, gmpy2.mpz_random(rand_state, range))
    index = gmpy2.mpz_random(rand_state, 1000)
    return (dig1023, index)

def otp():
    ''' Extracts a 6-digit otp from a self-generated random number starting from a random index.
    Prints the 1023 digit random number and the 6 digit OTP
    '''
    dig1023, index = generate()
    otp6 = int(str(dig1023)[index:index+6])
    print("1023 digit random number: ", dig1023)
    print("6 digit OTP: ", '{num:06d}'.format(num=otp6), "\n")

def main():
    # for i in range(100):
    #     otp()
    otp()

#start = time.time()
main()
#print("\n\n------------- "+ str(time.time() - start)+ " seconds --------------")