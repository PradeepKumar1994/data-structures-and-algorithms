
'''
Time complexity: O(n)
Space complexity: O(n)
'''
memory = []
def fibonacci(n):
    
    if(n <= 0):
        return 0

    if(n == 1):
        return 1

    return fibonacci(n-1)+fibonacci(n-2)
    

def _fib(n):
    memory = []

    for i in range(n+1):
        if(i <= len(memory)-1):
            memory[i-1] + memory[i-2]
        else:
            temp = fibonacci(i)
            print(temp)
            memory.append(temp)
    return memory

print(_fib(10))