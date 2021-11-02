
'''
Time complexity: O(V^2)
Space complexity: O(V)
'''

def inorder(arr):

    if(len(arr)<=1):
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        inorder(left)
        print('-->',arr[mid])
        inorder(right)

print(inorder([1,2,3,4,5,6,7,8,9, 10]))