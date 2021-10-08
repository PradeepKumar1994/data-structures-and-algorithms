

def permutate(string, substring):

    if(not len(string)):

        print('=----> subtring: ',substring)
        return None

    print('This is string: ', string)
    for i in range(len(string)):
        temp = string[i]
        left = string[0:i]
        right = string[i+1:]
        res = left+right
        permutate(res, substring+temp)

permutate('abc', '')
