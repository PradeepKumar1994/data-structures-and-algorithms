

'''
Time complexity: O(S)
Space complexity: O(S)
'''

def permutation(string, permutate_str):

    if(len(string)== 0):
        print(permutate_str)
        return None

    for i in range(0, len(string)):
        temp = string[i]
        remaining = string[0:i]+string[i+1:]
        permutation(remaining, permutate_str+temp)


def permutate(string):

    return permutation(string, '')


string = 'abc'
print(permutate(string))