#Problem3.py
#Project Euler problem 3

#from NumberTests import isPrime
#from NumberTests import getFactors

#def main():
  #number = 600851475143
  #factors = getFactors(number)
  #print(factors)

  #for f in factors:
    #if isPrime(f):
      #print(f)

#if __name__ == '__main__':
  #main()

"""Below is other code for it to work, I wasn't sure if we needed to modify it"""

from NumberTests import isPrime

def main():
    number = 600851475143
    largest = 0
    for i in range(1, int(number**0.5) + 1):
      if number % i == 0:
        if isPrime(i):
          largest = i
    print(largest)

if __name__ == '__main__':
    main()
