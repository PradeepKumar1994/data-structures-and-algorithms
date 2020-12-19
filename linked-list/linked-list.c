#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//declaration of methods
void insertion(void);
void print_value(void);
void insertionAtbeginning(void);
void insertionAtend(void);
void deleteAtend(void);
//variable declaration

struct node
{
    int value;
    struct node *next_addr; 
};

struct node *head, *temp_node, *new_node;
void main(void)
{

    int user_input, choice_loop = 1, user_loop = 1;
    char user_string[10];
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
            if(head==NULL)
            {
                printf("Insertion executing for initial node...\n");
                insertionAtbeginning();
            }
            else
            {
                user_loop = 1;
                while(user_loop == 1)
                {
                    
                    printf("Please enter the options for the following: \n");
                    printf("\tPlease enter [first]: to insert a node a begining of the list\n");
                    printf("\tPlease enter [last]: to insert a node at the end of the list\n");
                    
                    printf("Please enter your value: ");
                    scanf("%s", &user_string);

                    if(strcmp("first", user_string) == 0)
                    {
                        printf("Insertion executing..\n");
                        insertionAtbeginning();
                        user_loop = 0;
                        printf("Inserting the value at the beginning..\n");
                    }
                    else if(strcmp("last", user_string) == 0)
                    {
                        printf("Node insertion at end is initiated!");
                        insertion();

                        //printf("Do you wish to continue: [y/n]: ");
                        user_loop = 0;
                    }
                    else
                    {
                        printf("Your input is invalid. Please try again");
                        user_input = 1;
                    }
                    
                }
            }
        }

        else if(user_input == 2)
        {
            printf("Deletion executing");

            printf("Address: %p\n", temp_node);
            printf("Value is: %d\n", temp_node->value);

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

    if(head == NULL)
    {
        insertionAtbeginning();
    }
    else
    {
    
        //Comments used for debugging
        /*printf("Pointer: %p", new_node);*/
        printf("----> Address of previous node value %p", &new_node->value);
        new_node = (struct node*) malloc(sizeof(struct node));
        //new_node = (struct node*)Marshal.AllocHGlobal(sizeof(struct node)).ToPointer();
        printf("----> Address of current node value %p", &new_node->value);
        new_node->next_addr = 0;

        if(new_node != NULL)
        {
            printf("Please enter the value to be inserted: ");
            scanf("%d",&new_node->value);
            printf("Inserted value: %d", new_node->value);
            printf("Previous value: %d", temp_node->value); // THis is the key the values of old is still being sustained. - Start here.

            if(temp_node == head)
            {
                head->next_addr = new_node;
                //printf("Head next address: %p \n", head->next_addr);
                temp_node = new_node;
                temp_node->next_addr = 0;
                //printf("Temp_node current address: %p \n", temp_node);
                //printf("Temp_node next address: %p \n", temp_node->next_addr);

                print_value();
                //free(new_node); - DO NOT USE IT. FREE-ING CAUSES FREEING OF MEMORY SO YOU WOULD LOSE THE DATA AT THAT LOCATION.
            }
            else
            {
                printf("Sanity check: %p",&(temp_node->value));
                temp_node->next_addr = new_node;
                printf("Address of previous node Temp_node next address: %p \n", temp_node->next_addr);
                printf("Head next address: %p \n", head->next_addr);
                temp_node = new_node;
                printf("Temp_node new address: %p \n", temp_node);
            }
        }
    }
}

void insertionAtbeginning(void)
{
    
    if(head == 0)
    {
        //temp_node->value = 9999; - this will change the values of temp_node, head and new_node -
        // as they are pointing to the same address.
        //use the code from the insertion - you'll know what to do.

        new_node = (struct node*) malloc(sizeof(struct node));
        new_node->next_addr = 0;

        printf("Please enter the value to be inserted: ");
        scanf("%d",&new_node->value);
        printf("Inserted value: %d", new_node->value);
        
        //new_node->value = input;
        //printf("Sanity check: %p\n", new_node->value);
        head = temp_node = new_node;
        //printf("Sanity check: %p\n", new_node->value);
        //printf("Sanity check: %p\n", head->value);
    }
    else
    {
        
        new_node = (struct node*) malloc(sizeof(struct node));

        new_node->next_addr = head;

        head = new_node;

        printf("Please enter the value of");
        scanf("%d", &new_node->value);

        print_value();
        
    }    
}



void print_value(void)
{

    struct node *temp;
    temp = head;
    
    printf("#-------------------------------------------------\n");
    while(temp)
    {
        printf("Data of at %p node: %d \n", temp, temp->value);
        temp = temp->next_addr;
    }
    printf("#-------------------------------------------------");
}




/*

References - I found useful

    https://stackoverflow.com/questions/1169858/global-memory-management-in-c-in-stack-or-heap (refer again)



*/
