''' Meetakshi Setiya, 2019253
'''

import time
import random

def generate():
    '''Generates a 1023 digit random numbers. The probability that two generated numbers are equal is very low.
    Returns the generated randoom number
    '''
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    return(''.join(random.choice(numbers) for i in range(1023)))

def otp():
    '''Performs a random shuffle of the digits of a generated random number. 
    Extracts a 6-digit otp using the first 6 digits of the generated random number.
    Prints the 1023 digit random number and the 6 digit OTP
    '''
    dig1023 = generate()
    to_list = list(dig1023)
    random.shuffle(to_list)
    dig1023 = ''.join(to_list)
    otp6 = dig1023[:6]
    print("1023 digit random number: ", dig1023)
    print("6 digit OTP: ", otp6, '\n')
    
def main():
    # for i in range(100):
    #     otp()
    otp()

# start = time.time()
main()
# print("\n\n------------- "+ str(time.time() - start)+ " seconds --------------")