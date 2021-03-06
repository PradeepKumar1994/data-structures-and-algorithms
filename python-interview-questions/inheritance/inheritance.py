


class Employee:

    def __init__(self, name, organization, salary):

        self.name = name

        self.organization = organization

        self.salary = salary

    def display(self):

        print("Name: {} - Organization: {} - Salary: {}".format(self.name, self.organization, self.salary))

    @classmethod
    def employee_string(cls, emp_string):
        
        name, organization, salary = emp_string.split('-')

        return cls(name, organization, salary)


    @staticmethod
    def check_string(str_):

        if(str_ == 'Yes'):

            return 'Yes'
    
        else:
        
            return 'No'

class Engineer(Employee):

    def __init__(self, name, organization, salary, designation):

        super().__init__(name, organization, salary)

        self.designation = designation

    def display(self):

        print("Name: {} - Organization: {} - Salary: {} - Designation: {}".format(self.name, self.organization, self.salary, self.designation))



emp_string = 'Pradeep - Wazo - 28000'

gen_emp = Employee.employee_string(emp_string)

gen_emp.display()


print(gen_emp.check_string('Yes'))