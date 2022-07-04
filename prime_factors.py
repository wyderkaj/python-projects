import time

def get_prime_factors(N):
    factors = list()
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors
    
if __name__ == '__main__':
    print("Find the prime factorization of a given number")
    number = int(input("Please. Enter the number to be checked: "))
    time.sleep(1)
    print("Those are all yours prime numbers..")
    print(get_prime_factors(number))