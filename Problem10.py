#Problem10.py
#Project Euler problem 10

"""Find the sum of all the primes below two million."""
#Step 1: total starts at 2, the first prime number
#Step 2: loops, checks odd numbers from 3 up to 2 million looking at odds only
#Step 3: if the number is prime, returns True
#Step 4: True return, prime is added to total
#Step 5: prints total of all primes below 2 million
#Runtime notes: faster for smaller numbers, but takes a VERY long time for 2 million
from NumberTests import isPrime

def main():
  total = 2
  for i in range (3, 2000000, 2):
    if isPrime(i):
      total += i
  print(total)

if __name__ == '__main__':
  main()
