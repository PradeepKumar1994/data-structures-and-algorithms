#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//declaration of methods
void insertion(void);
void print_value(void);

//variable declaration

struct node
{
    int value;
    struct node *next_addr; 
};

struct node *head, *temp_node, *new_node;
head = NULL;
//head = 0;

void main(void)
{

    int user_input, choice_loop = 1;
    printf("head: %d", head);
    printf("Please enter [0]: to print values\n");
    printf("Please enter [1]: to insert\n");
    printf("Please enter [2]: to delete\n");
    printf("Please enter [3]: to exit\n");

    while(choice_loop)
    {
        printf("Please enter the information: ");
        scanf("%d", &user_input);
        if(user_input == 0)
        {
            printf("Printing values..");
            print_value();
        }
        
        else if(user_input == 1)
        {
            printf("Insertion executing..\n");
            new_node = (struct node*) malloc(sizeof(struct node));
            insertion();
        }

        else if(user_input == 2)
        {
            printf("Deletion executing");
        }    
        else if(user_input == 3)
        {
            printf("Exiting..");
            choice_loop = 0;
        }
        else
        {
            printf("Please re-enter your choice as per the instructions");
        }
        

    }
    
}

void insertion(void)
{
    //Used for debugging
    /*printf("Pointer: %p", new_node);*/
    printf("Pointer to current node: %p", new_node);
    printf("Pointer to next_node: %p", new_node->next_addr);
    
    printf("Please enter the value to be inserted: ");
    scanf("%d", new_node->value);

    new_node->next_addr = 0;

    if(head == 0)
    {
        temp_node = head = new_node;
        printf("Value of head: %d and value of next address %p\n", head, head->next_addr);
        }
    else if(temp_node == head)
    {
        head->next_addr = new_node;
        temp_node = new_node;
        temp_node->next_addr = 0;
    }
    else
    {
        temp_node->next_addr = new_node;
        temp_node = new_node;
    }
}

void print_value(void)
{
    struct node *print_temp;
    
    struct node *temp = *head;

    while(temp)
    {
        printf("temp_node: %p", *temp);

        printf("Data :");
        printf("%d, ", temp_node->value);
        temp = temp->next_addr;
    }

}
