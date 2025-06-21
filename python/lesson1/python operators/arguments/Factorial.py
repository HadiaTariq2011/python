def factorial(x):
    '''this is recursive function to find factorial or an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("factorial of 2:",factorial(4))