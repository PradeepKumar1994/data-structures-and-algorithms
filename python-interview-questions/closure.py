
#In Python you can return a function as an object - this is closure

def my_outer_function(message):

    def inner_function():

        print(message)

    return inner_function


func = my_outer_function('Hi')
func()

print('Name of the inner function: ',func.__name__)

func = my_outer_function('And this is closure')
func()


func = my_outer_function('Bye')
func()
