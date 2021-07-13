
from perm_copy import permutation

#CHAPTER ARRAYS - 
# INTERVIEW QUESTIONS 1.1

class permutations_two_string():

    def __init__(self,str1, str2):

        self.dict_ = {'str1': [], 'str2': []}

        self.str1 = str1

        self.str2 = str2

    def permutationx(self):

        self.dict_['str1'] = permutation(self.str1)
        self.dict_['str2'] = permutation(self.str2)

        for i in self.dict_['str1']:

            for j in self.dict_['str2']:

                if(i == j):

                    return "match found"


        return "No match found"



pts = permutations_two_string('str', 'rts')

pts.permutationx()
