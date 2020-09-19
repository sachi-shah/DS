# WAP to calculate factorial and to compute the factors of a given no. (i) using
# recursion, (ii) using iteration.

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

def iteration_factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return fact

print('Factorial of 5 using recursive function: ', recursive_factorial(5))
print('Factorial of 6 using iteration function: ', iteration_factorial(6))


def iteration_factors(x):
   print("The factors of ",x," are: ")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
            
def recursive_factors(n, i):
    if (i <= n): 
        if (n % i == 0): 
            print(i, end = " ")
        recursive_factors(n, i + 1)

print("\nFactors by iteration :")
iteration_factors(6)
print("Factors by recursion")
recursive_factors(8,1)






