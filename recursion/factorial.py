
'''
Time complexity: O(S)
Space complexity: O(S)
'''

def fact(n):

    if(n == 0):
        return 1

    if(n == 1):
        return 1

    else:
        return n * fact(n-1)

number = 5
print('Factorial of', number,'is:', fact(number))