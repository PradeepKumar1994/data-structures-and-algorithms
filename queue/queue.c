#include<stdbool.h>
#include<stdio.h>
#include<string.h>
#define MAX 9

void enqueue(int value, int enqueue_loop);
void print(void);
void dequeue(int enqueue_loop);
void queue_enqueue_order(int enqueue_loop);
void queue_dequeue_order(int enqueue_loop);

int queue_size; //size of the queue fluctues as the elements are inserted or deleted
int queue[MAX] = {0,0,0,0,0,0,0,0,0}; // a global array for queue
int queue_size_not_change; //size of the user pass as  a final reference

char *instruction_seq[4] = {"print", "push", "pop", "exit"};
bool loop = true;



void main(void)
{

    do
    {
        printf("Please enter the size of queue: ");
        scanf("%d", &queue_size);

    }while(queue_size < 1);
    
    printf("Queue_size is %d", queue_size);
    queue_size = queue_size - 1;
    queue_size_not_change = queue_size;

    
    char instruction[10];
    int value;

    //enqueue_loop is used to insert the element at a location & -
    //also used for something is which responsible for deleting the element
    int enqueue_loop = 0;   

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

            if(enqueue_loop == queue_size_not_change)
            {
                printf("The size of Queue is full!");
            }


            if(queue_size > -1)
            {
                
                for (enqueue_loop = enqueue_loop; enqueue_loop <= queue_size_not_change; enqueue_loop++)
                {
                    //pushing the elements into the queue structure
                    printf("Please enter the element ");
                    scanf("%d",&value);

                    enqueue(value, enqueue_loop);
                    queue_size--;  
                    enqueue_loop++;
                    
                    //Following loc is used as part of debugging
                    //printf("\nPrint the size of queue %d and enqueue loop %d", queue_size, enqueue_loop);

                    if(queue_size == -1)
                    {
                        enqueue_loop--;
                    }

                    break;
                }

            }
        }
        
        else if(strcmp(instruction, instruction_seq[2]) == 0)
        {

            if (enqueue_loop >= -1)
            {
                
                //pop function - removing the elements into the queue structure
                dequeue(enqueue_loop);

                enqueue_loop--;
                queue_size++;

                //Following loc is used as part of debugging
                //printf("Print the size of queue %d and enqueue loop %d", queue_size, enqueue_loop);

            }

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

void queue_enqueue_order(int enqueue_loop)
{
    int temp;
    for (int i = queue_size_not_change; i > -1; i--)
    {

        temp = queue[i];

        queue[i+1] = temp;

        queue[i] = 0;
        //queue[0] will remain the same - this is handled at enqueue

    }
    
}


void enqueue(int value, int enqueue_loop)
{

    if(enqueue_loop >= 0)
    {
        
        queue_enqueue_order(enqueue_loop);
        queue[0] = value;           //we replace the queue[0] with the first element

    }
    else if(enqueue_loop == -1)
    {
        queue[0] = value;
    }

    printf("The value %d, pushed into the queue", value);

}

void print(void)
{

    for (int i = 0; i <= queue_size_not_change; i++)
    {
        printf("%d ", queue[i]);
    }
    
}


void queue_dequeue_order(int enqueue_loop)
{
    int temp;

    for (int i = queue_size_not_change; i > -1; i--)
    {

        if(queue[i] != 0)
        {
            temp = queue[i];

            queue[i+1] = temp;

            queue[i] = 0;
        }
        
        //queue[0] will remain the same - this is handled at enqueue

    }
    
}



void dequeue(int enqueue_loop)
{
    
    if (queue_size ==-1)
    {
        printf("Removing %d from the queue", queue[queue_size_not_change]);

        queue_dequeue_order(enqueue_loop);

        queue[0] = 0;
    }
    
    else if(queue[queue_size_not_change]==0)
    {
        printf("Removing %d from the queue", queue[enqueue_loop]);
        
        queue_dequeue_order(enqueue_loop);

        queue[0] = 0;

    }
    else
    {
        printf("Removing the element %d",queue[queue_size_not_change]);

        queue_dequeue_order(enqueue_loop);

        queue[0] = 0;
    }

}