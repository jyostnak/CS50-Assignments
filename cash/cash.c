#include <cs50.h>
#include <stdio.h>

int main()
{
    int change;

    do
    {
        change = get_int("Change owed: ");
    }
    while (change <= 0);

    int coins = 0;

    while (change >= 25)
    {
        change -= 25;
        coins += 1;
    }

    while (change >= 10)
    {
        change -= 10;
        coins += 1;
    }

    while (change >= 5)
    {
        change -= 5;
        coins += 1;
    }

    while (change >= 1)
    {
        change -= 1;
        coins += 1;
    }
    printf("%i, %i", change, coins);
}
