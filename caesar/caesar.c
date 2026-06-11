#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argvc, string argv[])
{
    if (!(isdigit(argv[1])) || argc != 2)
    {
        printf("Usage: ./caesar key");
    }

    int k = atoi(argv);
    string text = get_string("plaintext: ")
    for (int i = 0; i < strlen(text); i++){
        int c = (text[i] + k) % 26
    }
}
