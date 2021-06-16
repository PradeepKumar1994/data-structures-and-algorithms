
#CHAPTER ARRAYS - 
# INTERVIEW QUESTIONS 1.1

class permutations_two_string():

    def __init__(self,str1, str2):

        self.array1 = []

        self.array2 = []

        self.str1 = str1

        self.str2 = str2

    def permutation(self):

        for i in range(len(self.str1)):

            for j in range(len(self.str2)):

                self.array1.append(self.str1[i] + self.str1[i+1:])
                print('-------------------------------------------------------------------')
                print(self.array1)
                print('-------------------------------------------------------------------')

                self.array2.append(self.str2[j] + self.str2[j+1:])
                print(self.array2)

                if(self.array1[-1] == self.array2[-1]):

                    return self.array1[-1], self.array2[-1]

            
pts = permutations_two_string("Pradeep", "Kumar")

pts.permutation()


