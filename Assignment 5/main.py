"""
Assignment #5 : Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
[Option step :  Print text 'Prime' if a number is prime]
"""

# Define function checkPrime to test a number is prime or not.
def checkPrime(num):
    if num > 1:
        #Check for factors
        for index in range(2, num):
            if (num % index) == 0:
                break
        else:
            print("prime")

# Logic for printing FizzBuzz from range 1 upto 100
for fizzbuzz in range(1,100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        #Validating prime number
        checkPrime(fizzbuzz)
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        #Validating prime number
        checkPrime(fizzbuzz)
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        #Validating prime number
        checkPrime(fizzbuzz)
        continue
    print(fizzbuzz)
    # Validating prime number
    checkPrime(fizzbuzz)
