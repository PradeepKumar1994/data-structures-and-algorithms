
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    print('string:', lst)
    for i in range(len(lst)):
       m = lst[i]
       print('m: ', m)
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
       
       print('lst[:i] ',lst[:i]) 
       print('lst[i+1:] ',lst[i+1:]) 
       print('remLst: ',remLst) 
       # Generating all permutations where m is first
       # element
       temp = permutation(remLst)
       print('----->',temp)
       for p in temp:
           print('p: ',p)
           print('--',[m] + p)
           l.append([m] + p)
    return l
 
''' 
# Driver program to test above function
data = list('abc')
result = []
for p in permutation(data):
    print(p)
    result.append(p)

'''