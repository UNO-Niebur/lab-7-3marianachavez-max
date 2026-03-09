#Problem7.py
#Project Euler problem 7

"""What is the 10001st prime number?"""
#Step 1:#stores prime numbers
#Step 2: #checks numbers from 2 up to the nth prime number
#Step 3: #loops until nth prime
#Step 4: #increments number to check
#Step 5: #if the number is prime, then, 
#Step 6: #adds to list
#Step 7: #returns the last prime, which is nth prime
#Step 8: #prints the 10001st prime number
#Runtime notes: faster for smaller numbers, but is efficient when testing 10001

from NumberTests import isPrime

def findNthPrime(n): #I originally had this as a helper function, but it wasn't reused so I made it a main function.
  """Returns the nth prime number"""

  nums = [] 
  i = 1 
  while len(nums) < n: 
     i += 1 
     if isPrime(i): 
        nums.append(i) 

  return nums[-1] 

def main():
  print(findNthPrime(10001))

if __name__ == '__main__':
  main()
