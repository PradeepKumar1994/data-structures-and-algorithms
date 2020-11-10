#include<stdio.h>
#include<string.h>
#include<stdbool.h>

#define MAX 9

int push(int value);
void pop(void);
void printing(void);

int stack[MAX] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
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

    stack_size_not_change = stack_size;
    printf("Size of the stack is %d \n", stack_size);

    while(int_type)
    {
        char operation[5];
        printf("Please enter for your options: ");
        scanf("%s", &operation);
        int_type = 1;

        if(strcmp(operation, stack_operations[0]) == 0)
        {
            
            if(stack_size == 0)
            {

                printf("-----Stack is full! Please clear few elements----\n");
            }

            else if(stack_size > 0)
            {
                do
                {
                    printf("\n Please enter the value to push: ");
                    scanf("%d", &push_value);

                }while (stack_size<0);
                
                push(push_value);
                stack_size-- ;
            }
        }

        else if (strcmp(operation, stack_operations[1]) == 0) // pop 
        {
            if(stack_size  == stack_size_not_change)
            {
                printf("Stack underflow has occurred, since no elements in the stack");
            }
            else
            {                
                pop();
            }
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
    
    stack[stack_size-1] = (value);

    printf("Value: %d inserted at %d", value, stack[stack_size-1]);
}

void printing(void)
{

    printf("Stack elements are: ");
    
    for(int i = stack_size_not_change-1; i >= 0; i--)
    {
        printf("%i ", stack[i]);
    }

}

void pop(void)
{

    printf("Pop entered!");

    printf("Element in the Stack %d", stack[stack_size]);

    stack[stack_size] = NULL;
                
    //incrementing the size of stack as elements are removed
    stack_size++ ;                  
                
    printf("Size of stack_size %d", stack_size);
}

//int overflow(void);
//int underflow(void);