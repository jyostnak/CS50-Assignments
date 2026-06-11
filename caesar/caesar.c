#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    printf("ciphertext: ");

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);
    string text = get_string("plaintext: ");
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            char c = ((text[i] - 'A' + k) % 26) + 'A';
            printf("%c", c);
        }
        else if (islower(text[i]))
        {
            char c = ((text[i] - 'a' + k) % 26) + 'a';
            printf("%c", c);
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}
