

array = []

def permutations(str_):

    temp = ''

    for i in range(len(str_)):

        try:

            if(i>0):

                temp = str_[-1 * len(str_):i]

        except:

            temp = ""

        temp1 = str_[i]+str_[i+1:]+temp

        if(temp1 not in array):

            array.append(temp1)

            return permutations(temp1)

    return array


print(permutations('abc'))