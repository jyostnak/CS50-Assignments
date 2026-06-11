#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int get_score(string word);

int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");

    if (get_score(player_1) > get_score(player_2))
    {
        printf("Player 1 wins!");
    }
    else if (get_score(player_1) < get_score(player_2))
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
}

int get_score(string word)
{
    int score = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            score += points[word[i] - 'A'];
        }

        else if (islower(word[i]))
        {
            score += points[word[i] - 'a'];
        }
    }
    return score;
}
