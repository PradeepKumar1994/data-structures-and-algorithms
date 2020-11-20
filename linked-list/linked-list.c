#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 9

//declaration of methods
void insertion(void);

//variable declaration

struct node
{
    int value;
    struct node *next_addr; 
};

struct node *head;
struct node *new_node;


void main(void)
{

    int user_input, choice_loop  = 1;
    printf("Please enter [0]: to print values\n");
    printf("Please enter [1]: to insert\n");
    printf("Please enter [2]: to delete\n");
    printf("Please enter [3]: to exit\n");

    printf("Please enter the information: ");
    scanf("%d", &user_input);

    while(choice_loop)
    {
        if(user_input == 0)
        {
            printf("Printing values..");
            break;
        }
        
        else if(user_input == 1)
        {
            printf("Insertion executing..\n");
            insertion();
            break;
        }

        else if(user_input == 2)
        {
            printf("Deletion executing");
            break;
        }    
        else if(user_input == 3)
        {
            printf("Exiting..");
            choice_loop = 0;
            break;
        }
        else
        {
            printf("Please re-enter your choice as per the instructions");
            break;
        }
        

    }
    
}

void insertion(void)
{
    new_node = (struct node*) malloc(sizeof(struct node));
    printf("Pointer: %p", malloc(sizeof(struct node)));
    printf("Please enter the value to be inserted: ");
    scanf("%d", new_node->value);

    new_node->next_addr = 0;

    printf("Values are entered");
}