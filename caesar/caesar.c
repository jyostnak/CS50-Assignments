#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, string argv[])
{
    if (!(isdigit(argv[1])) || argc != 2)
    {
        printf("Usage: ./caesar key");
    }

    int k = atoi(argv);
    string text = get_string("plaintext: ")
    for (int i = 0; i < strlen(text); i++){
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
}
