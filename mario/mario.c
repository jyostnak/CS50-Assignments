#include <stdio.h>
#include <cs50.h>

int main()
{
    int height;
    do{
        height = get_int("Height: ");
    }while(height<=0);

    for(int row = 1; row <= height; row++){
        for (int s = 0; s<=height-row-1; s++){
            printf(" ");
        }
        for (int r = 0; r<row; r++){
            printf("#");
        }
        printf("\n");
    }
}
