
'''
Time complexity: O(2^n)
Space complexity: O(n)
'''

def subset(string, rem):

    if(string ==  ''):
        print('value: ',rem)
        return None

    temp = string[0]
    substr = string[1:]
    subset(substr, rem+temp)
    subset(substr, rem)

subset('abc','')
