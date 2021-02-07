

#stack

class Stack(object):

    def __init__(self):

        self.stack = []

        self.input_element = {'{':0, '}':0, '[':0, ']':0, '(':0, ')': 0}

    def push(self, value):

        for i in self.input_element:

            if(value == i):
                
                self.stack.append(value)
            
            else:

                print("valid input")
                

    def pop(self): #pop

        for i in self.stack:

            temp = self.stack.pop()

            for i in self.input_element.keys():

                if(temp == i):

                    self.input_element[i] = self.input_element[i] + 1


        return None

    def validation(self):
        temp_stack = []
        for i in range(len(self.input_element.values)):

            pass
                

            

            

    def print_all(self):

        pass

    def exit(self):

        pass
