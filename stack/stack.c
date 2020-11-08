#include<stdio.h>
#include<string.h>
#include<stdbool.h>

#define MAX 9

int push(int value);
int pop(void);
int overflow(void);
int underflow(void);

int stack[MAX];
int stack_size = 0;
int stack_size_not_change = 0;
char *stack_operations[4] = {"push", "pop", "printing", "exit"};
int int_type = 1;
void main(void)
{

    int push_value;
    do
    {
//        printf("Please enter an integer input for the size of the stack:  ");
//        scanf("%d", &stack_size);
        printf("Please enter the size of the stack:  ");
        scanf("%d", &stack_size);
    } while (stack_size < 0);
    

    printf("Size of the stack is %d \n", stack_size);

    while(int_type)
    {
        char operation[5];
        printf("Please enter for your options: ");
        scanf("%s", &operation);
        int_type = 1;

        if(strcmp(operation, stack_operations[0]) == 0)
        {
            if(stack_size > 0)
            {
                do
                {
                    printf("\n Please enter the value to push: ");
                    scanf("%d", &push_value);

                }while (stack_size<0);
                
                stack_size_not_change = stack_size;

                if(!push(push_value))
                {
                    
                    printf("Value inserted in the stack should be greater than -1\n");

                }

            }
            
            if(stack_size == 0)
            {

                printf("----Stack is full! Please clear few elements.----");
            }
        }

        else if (strcmp(operation, stack_operations[1]) == 0) // pop 
        {
            stack_size = stack_size - 1;//incrementing the size of stack as elements are removed
            
            printf("Pop entered\n");
        }

        else if(strcmp(operation, stack_operations[2]) == 0) //print
        {
            printf("Printing all elements in stack\n");
            printing();
        }

        else if(strcmp(operation, stack_operations[3]) == 0)
        {
            printf("Exiting from program, deleting all elements..\n");
            printf("Stack is empty\n");
            printf("Goodbye\n");
            int_type = 0;
        }

        //later incorporate the bool type
        else
        {
            int_type = 1;
        }
   
    }
}

int push(int value)
{

    if(value < 0)
    {
        return 0;
    }

    stack[i] = value;
    return 1;
}

int printing(void)
{

    printf("Stack elements are: ");

    //printf("%d", stack[1]);

    //printf("%d", stack[0]);
    
    for(int i = MAX; i > -1; i--)
    {
        printf("%i ", stack[i]);
    }


}


//int pop(void);
//int overflow(void);
//int underflow(void);