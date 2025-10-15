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

typedef struct Node {
    Bank account;
    struct Node *next;
} Node;

Node *start = NULL;
Node *current = NULL;
Node **indirect = &start;
FILE *fpdata;

/* Function prototypes */
void showMenu();
void appendAccountToList(Bank);
void readAccountDetails(Bank*);
void saveIntoFile();
void load();
void create();
void read();
void showAccount(Node*);
Node* findAccount();
Node* search(char*);
void updateNode(Node*);
void deleteNode(Node*);
void edit();

/* ---------------------- MENU ---------------------- */
void showMenu()
{
    int choice;
    do 
    {
        clear();
        printf("\n--- MENU ---\n1. Save Account \n2. Show Accounts \n3. Edit Account\n4. Exit\n---------------\nEnter choice: ");
        scanf("%d", &choice);
        getchar();
        switch (choice) 
        {
            case 1: create(); break;
            case 2: read(); break;
            case 3: edit(); break;
            case 4: printf("Exiting...\n"); exit(0);
            default: printf("Invalid choice!\n"); pause();
        }

    } while(choice != 4);
}

/* ---------------------- BASIC FUNCTIONS ---------------------- */
void readAccountDetails(Bank *account)
{   
    printf("Enter Account Number: ");
    readText(account->accountNumber, 15);
    printf("Enter Name: ");
    readText(account->name, 20);
    printf("Enter Balance: ");
    readFloat(&account->balance);
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
    Node *cur = start;
    while(cur != NULL)
    {
        fwrite(&cur->account, sizeof(Bank), 1, fpdata);
        cur = cur->next;
    }
    fclose(fpdata);
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

void create()
{
    Bank account;
    readAccountDetails(&account);
    appendAccountToList(account);
    saveIntoFile();
    printf("Account added successfully!\n");
    pause();
}

void read() 
{
    Node *cur = start;
    if (cur == NULL) 
    {
        printf("No accounts available.\n");
        pause();
        return;
    }

    while (cur != NULL) 
    {
        showAccount(cur);
        cur = cur->next;
    }
    pause();
}

void showAccount(Node* pNode)
{
    printf("----------------------------------------------\n");
    printf("Node Address : %p\n", (void*)pNode);
    printf("%-15s %-20s %-10s\n", "Account No", "Name", "Balance");
    printf("%-15s %-20s %.2f\n", pNode->account.accountNumber, pNode->account.name, pNode->account.balance);
}

/* ---------------------- SEARCH + FIND ---------------------- */
Node* search(char* idToSearch)
{
    Node *cur = start;
    while(cur != NULL)
    {
        if(strcmp(cur->account.accountNumber, idToSearch) == 0)
            return cur;
        cur = cur->next;
    }
    return NULL;
}

Node* findAccount()
{
    char idToSearch[15];
    printf("Enter Account Number to search: ");
    readText(idToSearch, 15);

    Node *found = search(idToSearch);
    if (found != NULL)
    {
        printf("Account found!\n");
        showAccount(found);
    }
    else
    {
        printf("Account not found!\n");
    }
    pause();
    return found;
}

/* ---------------------- UPDATE + DELETE ---------------------- */
void updateNode(Node* pNode)
{
    if (pNode == NULL) {
        printf("Invalid node. Cannot update.\n");
        return;
    }

    printf("Updating account:\n");
    showAccount(pNode);

    printf("Enter new name: ");
    readText(pNode->account.name, 20);
    printf("Enter new balance: ");
    readFloat(&pNode->account.balance);

    saveIntoFile();
    printf("Account updated successfully!\n");
    pause();
}

void deleteNode(Node* pNode) 
{ 
    if (start == NULL) {
        printf("Please load data first.\n");
        return;
    }

    Node *current = start;
    Node *prev = NULL;
    int found = 0;

    showAccount(pNode);

    while (*indirect != pNode) 
    {
        indirect = &(*indirect)->next;
    }
    *indirect = pNode->next;
   

    free(current);
    saveIntoFile();
    printf("Account deleted successfully!\n");
    pause();
}

/* ---------------------- EDIT MENU ---------------------- */
void edit()
{
    Node *foundNode = findAccount();

    if (foundNode != NULL) 
    {
        int choice;
        do
        {
            printf("\nEdit Menu\n-----------\n1. Update\n2. Delete\n3. Cancel\nEnter your choice: ");
            scanf("%d", &choice);
            getchar();

            switch(choice)
            {
                case 1: updateNode(foundNode); break;
                case 2: deleteNode(foundNode); return; // stop after deletion
                case 3: printf("Cancelled.\n"); return;
                default: printf("Invalid choice.\n");
            } 
        } while(choice != 3);
    }
    else 
    {
        printf("\nNo account found to update or delete.\n");
        pause();
    }
}

/* ---------------------- MAIN ---------------------- */
int main()
{
    clear();
    load(); 
    showMenu();
    return 0;
}
