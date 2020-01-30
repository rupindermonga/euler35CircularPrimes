#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

def isPrime(n):
    result = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result = False
            break
    return result

def rotation(n):
    rotations = set()
    for i in range(len(str(n))):
        new_variation = int(str(n)[i:] + str(n)[:i])
        rotations.add(new_variation)
    return rotations

def isCircularPrime(n):
    new_set = rotation(n)
    result = True
    for eachSet in new_set:
        if not isPrime(eachSet):
            result = False
    return result

def CircularPrimes(n):
    #below n finding all circular primes
    notCirPrimeSet = set()
    CirPrimeSet = set()
    for i in range(2,n):
        new_set = rotation(i)
        if (new_set & notCirPrimeSet):
            pass
        elif (new_set & CirPrimeSet):
            pass
        elif isCircularPrime(i):
            CirPrimeSet |= new_set
        else:
            notCirPrimeSet |= new_set
    return len(CirPrimeSet)
            

final = CircularPrimes(1000000)
print(final)