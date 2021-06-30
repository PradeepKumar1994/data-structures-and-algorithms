
def fact(n):

    if(n == 1):

        return n

    else:

        return n* fact(n-1)


class Permutations():

    def __init__(self, str_):

        self.original_str_ = str_

        self.str_ = str_

        self.queue = []

        self.length_str = len(str_)

        self.factorial_max = fact(self.length_str)

        print(self.factorial_max)

    def permutations_words(self):

        if(len(self.queue) == self.factorial_max):

            return self.queue

        else:

            if(self.str_ not in self.queue):

                print(self.str_)

                self.queue.append(self.str_)

                str_rev = self.str_[::-1]

                print(str_rev)

                self.queue.append(str_rev)

                self.str_ = self.str_[-1]+self.str_[:-1]

                return self.permutations_words()



perm = Permutations('abc')

print(perm.permutations_words())

print('Runtime should be log N')