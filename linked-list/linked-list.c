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
    new_node = (struct node*) malloc(sizeof(struct node));
    //new_node = (struct node*)Marshal.AllocHGlobal(sizeof(struct node)).ToPointer();
    printf("Pointer to current node: %p \n", new_node);
    printf("Pointer to next_node: %p  \n", new_node->next_addr);
    new_node->next_addr = 0;

    printf("Please enter the value to be inserted: ");
    scanf("%d", &new_node->value);
    printf("Inserted data is: %d \n", new_node->value);

    if(head == 0)
    {
        temp_node = head = new_node;
        //temp_node->value = 0;
        printf("Value of head: %d and value of next address %p\n", head->value, head->next_addr);
        printf("Value of Temp_node: %d and value of next address %p\n", temp_node->value, temp_node->next_addr);
        printf("Value of new_node: %d and value of next address %p\n", new_node->value, new_node->next_addr);
        }
    else if(temp_node == head)
    {
        head->next_addr = new_node;
        printf("Head next address: %p \n", head->next_addr);
        temp_node = new_node;
        temp_node->next_addr = 0;
        printf("Temp_node current address: %p \n", temp_node);
        printf("Temp_node next address: %p \n", temp_node->next_addr);
    }
    else
    {
        temp_node->next_addr = new_node;
        printf("Address of previous node Temp_node next address: %p \n", temp_node->next_addr);
        temp_node = new_node;
        printf("Temp_node new address: %p \n", temp_node);
    }
}

void print_value(void)
{

    struct node *temp;
    temp = head;
    printf("#-------------------------------------------------\n");
    while(temp)
    {
        //debugging purposes
        printf("temp_node next address: %p \n", temp->next_addr); 
        //debugging purposes
        printf("Data of current node: %d \n", temp_node->value);
        temp = temp->next_addr;
    }
    printf("#-------------------------------------------------");
}




/*

References - I found useful

    https://stackoverflow.com/questions/1169858/global-memory-management-in-c-in-stack-or-heap (refer again)

    https://stackoverflow.com/questions/39201738/getting-garbage-values-while-implementing-linked-list-using-structs-in-c-sharp#



*/
