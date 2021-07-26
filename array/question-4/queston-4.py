
class Question4():

    def __init__(self, input_str):

        self.str_ = input_str

    def palindrome(self, string_):

        if(len(string_) != len(self.str_)):

            return False

        print('Palindrome check running..')

        count = 0
        string_rev = string_[::-1]

        print('Reversed string: ', string_rev)
        print('Original string: ', string_)
 
        if(len(self.str_) != len(string_rev)):

            print('This executed')
    
            return False 

        else:

            for i in range(len(self.str_)):

                if(self.str_[i] == string_rev[i]):

                    count = count + 1

            if(count == len(string_rev)):

                return True

    def permutate(self, str_):

        l = []

        sub_str = ''

        if(len(str_) == 0):

            print('Empty string')

        for i in range(len(str_)-1):

            temp = str_[i]

            sub_str =  str_[:i]+str_[i+1:]

            result_permutate = self.permutate(sub_str)

            if(not len(result_permutate) < len(self.str_)-2):

                for i in result_permutate:
            
                    l.append(temp+i)

                    if(self.palindrome(l[-1])):

                        print("Palindrome")

                        return l

        return sub_str


    def run(self):

        result = self.permutate(self.str_)

        return result

print('----------------')

ques = Question4('tenet')

ques.run()