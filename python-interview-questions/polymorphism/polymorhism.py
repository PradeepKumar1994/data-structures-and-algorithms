class Employee:    def __init__(self, name):        self.name = name    def name(self):        passclass Clerk(Employee):    def __init__(self, name):        self.name = name    def name(self):        print(self.name)c = Clerk('Pradeep')print(c.name)print(isinstance(Clerk, Employee))