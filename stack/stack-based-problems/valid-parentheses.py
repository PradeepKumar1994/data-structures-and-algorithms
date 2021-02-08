

#stack

class Stack(object):

    def __init__(self):

        self.stack = []

        self.input_element = {'{':0, '}':0, '[':0, ']':0, '(':0, ')': 0}

    def push(self, value):

        for i in self.input_element:

            if(value == i):
                
                self.stack.append(value)
            

    def pop(self): #pop

        for i in self.stack:

            temp = self.stack.pop()

            for i in self.input_element.keys():

                if(temp == i):

                    self.input_element[i] = self.input_element[i] + 1


        return None

    def validation(self):

        temp_stack_keys =  self.input_element.keys()
        temp_stack_values =  self.input_element.values()
        print(temp_stack_values)
        for i in range(0, len(temp_stack_keys), 2):

            if(i %2 == 0):
                print(temp_stack_values[i])
                decide = temp_stack_values[i] - temp_stack_values[i+1]

                if(decide != 0):

                    return "In Valid"

        return "Valid"


            

    def print_all(self):

        for key, values in self.input_element.items():

            print(values)

            

    def exit(self):

        pass




stack = Stack()


stack.push('{')
stack.push('{')
stack.push('}')
stack.push('}')
stack.print_all()
stack.validation()

