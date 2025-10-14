#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void clear()
{
    system("cls");
}

void pause() {
    system("pause");
}

void removenewline(char *text) {
    text[strcspn(text, "\n")] = '\0';
}

void readText(char *text, int length)
{
    fgets(text, length, stdin);
    removenewline(text);
}

void readFloat(float* number)
{
    scanf("%f", number);
    getchar();
}