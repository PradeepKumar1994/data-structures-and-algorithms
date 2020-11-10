#include<stdbool.h>
#include<stdio.h>
#include<string.h>
#define MAX 9
int queue_size;
int queue[MAX];

char *instruction_seq[4] = {"print", "enqueue", "dequeue", "exit"};
bool loop = true;

void main(void)
{

    printf("Enter the size of the queue: ");
    scanf("%d", &queue_size);

    while(loop)
    {
        char instruction[10];
        printf("Please enter your instruction type: ");
        scanf("%d", instruction);

        if(strcmp(instruction, instruction_seq[0]) ==0 )
        {
            printf("we print elements here");
        }
        
        else if (strcmp(instruction, instruction_seq[3]) == 0)
        {
            printf("Exiting..");
            loop = false;
        }
        
        
    }

}