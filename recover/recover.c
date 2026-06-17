#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card
    FILE *img = NULL;
    int jpg_count = 0;
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff &&
        buffer[1] == 0xd8 &&
        buffer[2] == 0xff &&
        (buffer[3] & 0xf0) == 0xe0)
        {
            // If we're already writing a JPEG,
            // close it before starting a new one
            if (img != NULL)
            {
            fclose(img);
            }

            // Create filename: 000.jpg, 001.jpg, ...
            char filename[8];
            sprintf(filename, "%03i.jpg", jpg_count);
            // Open the new JPEG file
            img = fopen(filename, "w");
            // Increase jpg_count
            jpg_count++;
        }

        // If a JPEG file is currently open,
        // write this 512-byte block to it
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    fclose(img);
    fclose(card);
}

