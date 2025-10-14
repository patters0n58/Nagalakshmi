#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tools.c"

#define DATAFILE "accounts2.dat"

typedef struct {
    char accountNumber[15];
    char name[20];
    float balance;
} Bank;

typedef struct Node{
    Bank account;
    struct Node *next;
}Node;

Node *start = NULL;
Node *current = NULL;

FILE *fpdata;

void showMenu();
void create();
void read();
void update();
void delete();
void load();
void appendAccountToList(Bank);
void readAccountDetails(Bank*);
void saveIntoFile();


void showMenu()
{
    int choice;
    do 
    {
        clear();
        printf("\n--- MENU ---\n1. Save Account \n2. Show Accounts \n3. Update Accounts \n4. Delete Accounts\n5. Exit\n---------------\nEnter choice: ");
        scanf("%d", &choice);
        getchar();
        switch (choice) 
        {
            case 1: create(); break;
            case 2: read(); break;
            case 3: update(); break;
            case 4: delete(); break;
            case 5: printf("Exiting...\n"); exit(0);
            default: printf("Invalid choice!\n");
        }

    }while(choice != 5);
}

void readAccountDetails(Bank *account)
{   
    printf("Enter Account Number: ");
    readText(account->accountNumber, 15);
    printf("Enter Name: ");
    readText(account->name, 20);
    printf("Enter Balance: ");
    readFloat(&account->balance);
    pause();
}

void appendAccountToList(Bank pAccount)
{
    Node *newNode = malloc(sizeof(Node));
    newNode->account = pAccount;
    newNode->next = NULL;

    if (start == NULL) {
        start = current = newNode;
    } else {
        current->next = newNode;
        current = newNode;
    }
}

void saveIntoFile()
{
    fpdata = fopen(DATAFILE, "wb");
    if (!fpdata) {
        printf("Error opening file!\n");
        return;
    }
    Node *current = start;
    while(current != NULL)
    {
        fwrite(&current->account, sizeof(Bank), 1, fpdata);
        current = current->next;
    }
    fclose(fpdata);
}

void create()
{
    Bank account;
    readAccountDetails(&account);
    appendAccountToList(account);
    saveIntoFile();
    printf("Account added successfully!\n");
    pause();
}

void load() {
    FILE *fp = fopen(DATAFILE, "rb");
    if (!fp) {
        printf("No data file found.\n");
        return;
    }

    Bank accountx;
    while (fread(&accountx, sizeof(Bank), 1, fp) == 1) {
        appendAccountToList(accountx);
    }

    fclose(fp);
}

void read() 
{
    Node *current = start;
    if (current == NULL) 
    {
        printf("No accounts available.\n");
        pause();
        return;
    }
    else
    {
        printf("\n%-15s %-20s %-10s\n", "Account No", "Name", "Balance");
        printf("----------------------------------------------\n");
        while (current != NULL) 
        {
            printf("%-15s %-20s %.2f\n", current->account.accountNumber, current->account.name, current->account.balance);
            current = current->next;
        }
    pause();
    }
}

void update() 
{ 
    int found = 0;
    char idToUpdate[15];
    Node *current = start;

    printf("Enter account number to update: ");
    readText(idToUpdate, 15);

    while(current != NULL)
    {
        if(strcmp(current->account.accountNumber, idToUpdate) == 0)
        {
            found = 1;
            printf("\n1. Enter new name\n2. Enter new balance\nEnter your choice: ");
            char choice = getchar();
            getchar();
            switch(choice)
            {
                case '1':
                    printf("Enter new name: ");
                    readText(current->account.name, sizeof(current->account.name));
                    break;

                case '2':
                    printf("Enter new balance: ");
                    readFloat(&current->account.balance);
                    break;

                default:
                    printf("Invalid choice!\n");
                    break;
            }

            saveIntoFile();
            printf("Account updated successfully!\n");
            break;
        } 
        current = current->next;
    }

    if (!found)
    {
        printf("Account not found!\n");
    }

    pause(); 
}


void delete() 
{ 
    if (start == NULL) {
        printf("Please load data first.\n");
        return;
    }

    char idToUpdate[15];
    printf("Enter Account Number to delete: ");
    readText(idToUpdate, 15);

    Node *current = start;
    Node *prev = NULL;
    int found = 0;

    while (current != NULL) 
    {
        if (strcmp(current->account.accountNumber, idToUpdate) == 0) {
            found = 1;
            if (prev == NULL) {
                start = current->next;
            } else {
                prev->next = current->next;
            }
            free(current);

            saveIntoFile();
            printf(" Account deleted successfully!\n");
            break;
        }
        //prev = current;
        current = current->next;
    }

    if (!found)
        printf("Account not found.\n");
}

int main()
{
    clear();
    load();
    showMenu();
}
