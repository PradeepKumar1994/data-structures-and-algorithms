
class Question4():

    def __init__(self, input_str):

        self.str_ = input_str

    def palindrome(self, string_):

        print('Palindrome check running..')

        count = 0
        string_rev = string_[::-1]
 
        if(len(self.str_) != len(string_rev)):

            return False 

        else:

            for i in range(len(self.str_)):

                if(self.str_[i] == string_rev[i]):

                    count = count + 1

            if(count == len(string_rev)):

                return True

    def permutate(self, str_):

        l = []

        for i in range(len(str_)):

            temp = str_[i]

            sub_str =  str_[:i]+str_[i+1:]

            result_permutate = self.permutate(sub_str)

            for i in result_permutate:

                l.append(m+i)

                print(l[-1])

                if(self.palindrome(l[-1])):

                    print("Palindrome")

                    return True

        return l



ques = Question4('ENET')

ques.permutate('ENET')