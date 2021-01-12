def sieve(num):
    """
    This function uses sieve of eratosthenes algorithm to compute 
    a list of prime numbers within a range.

    @param: Integer - num
    @return: List of integers.
    """

    # Initialize variables.
    prime_num = list()

    # Create a list True values the size of num
    prime_bol = [True for i in range(num + 1)] 
    p = 2
    while (p * p <= num): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime_bol[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, num + 1, p): 
                prime_bol[i] = False
        p += 1
    prime_bol[0]= False
    prime_bol[1]= False
    # Print all prime numbers 
    for p in range(num + 1): 
        if prime_bol[p]: 
            prime_num.append(p)
    return prime_num
  

def main():
    # Request input from user and get prime numbers up to the input.
    print(f'The primes are:\n{sieve(int(input("Enter an integer: ")))}')

if __name__=='__main__': 
    main()