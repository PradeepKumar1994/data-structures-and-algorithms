
'''
Time complexity: O(S)
Space complexity: O(S)
'''

def palindrome(str):

    if(len(str)==0):
        return True
    else:
        if(str[0]==str[-1]):
            return palindrome(str[1:len(str)-1])

    return False


print(palindrome('aaab'))