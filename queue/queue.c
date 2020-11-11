#include<stdbool.h>
#include<stdio.h>
#include<string.h>
#define MAX 9

void enqueue(int value);
void print(void);
void pop(void);

int queue_size;
int queue[MAX] = {0,0,0,0,0,0,0,0,0};
int queue_size_not_change;

char *instruction_seq[4] = {"print", "push", "pop", "exit"};
bool loop = true;


void main(void)
{

    do
    {
        printf("Please enter the size of queue: ");
        scanf("%d", &queue_size);

    }while(queue_size < 1);
    
    queue_size_not_change = queue_size;

    
    char instruction[10];
    int value;

    while(loop)
    {
        printf("Please enter your instruction type: ");
        scanf("%s", &instruction);

        if(strcmp(instruction, instruction_seq[0]) == 0 )
        {
            
            printf("Printing elements \n");

            print();

        }

        else if(strcmp(instruction, instruction_seq[1]) ==0 )
        {

            //pushing the elements into the queue structure

            printf("Please enter the element ");
            scanf("%d",&value);

             enqueue(value);
            queue_size-- ;

        }
        
        else if(strcmp(instruction, instruction_seq[2]) == 0)
        {
            //removing the elements into the queue structure
            printf("we remove elements for this function");
            
            pop();
        }

        else if (strcmp(instruction, instruction_seq[3]) == 0)
        {
            printf("Exiting..");
            loop = false;
        }

        else
        {
            loop = true;
        }   
    }
}

void enqueue(int value)
{

    queue[queue_size - 1] = value;

    printf("The value %d, pushed into the queue", value);

}

void print(void)
{

    for (int i = 0; i < queue_size_not_change; i++)
    {
        printf("%d ", queue[i]);
    }
    
}

void pop(void)
{
    
    printf("this is working \n");

    printf("Removing %d from the queue", queue[queue_size_not_change-1]);

    queue[queue_size_not_change-1] = 0;

    queue_size++;
}