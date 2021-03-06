
#CHAPTER ARRAYS - 
# INTERVIEW QUESTIONS 1.

class Unique():

    def __init__(self, str_):

        self.queue = []
        self.str_ = str_
        self.low_ = {}

        for i in range(97,123):

            self.low_[i] = 0

    def run(self):

        str_lower = self.str_.lower()

        for i in str_lower:

            temp = ord(i)

            self.low_[temp] = 1


        for key, value in self.low_.items():

            if(value > 0 and chr(key) not in self.queue):
                self.queue.append(chr(key))

        return self.queue



string = input("Please enter a string: ")

unique_ = Unique(string)

return_value = unique_.run()

print(return_value)

print('Run time complecity is: time expected to run string to lower + O(N)')