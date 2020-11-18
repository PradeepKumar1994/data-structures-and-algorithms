#include<stdio.h>
#include<string.h>
#define MAX 9
//declaration of methods


//variable declaration

struct node
{
    int value;
    struct node *next_addr; 
};

struct node lists[MAX];


struct node *head;


void main(void)
{
    int user_input;
    printf("Please enter [0]: to print values\n");
    printf("Please enter [1]: to insert\n");
    printf("Please enter [2]: to delete\n");
    printf("Please enter [3]: to exit\n");

    printf("Please enter the information: ");
    scanf("%d", &user_input);

    if(user_input == 0)
    {
        printf("Printing values..");
    }
    
    else if(user_input == 1)
    {
        printf("Insertion executing");
    }

    else if(user_input == 2)
    {
        printf("Deletion executing");
    }    
    else if(user_input == 3)
    {
        printf("Exiting..");
    }    


}