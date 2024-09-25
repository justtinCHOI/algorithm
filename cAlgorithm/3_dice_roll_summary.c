#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROLLS 60000

int main() {
    int dice[6] = {0}; // Array to store dice results
    int roll, i;

    // Initialize random seed
    srand(time(NULL));

    // Roll the dice 60000 times
    for (i = 0; i < ROLLS; i++) {
        roll = rand() % 6; // Random value between 0 and 5
        dice[roll]++;
    }

    // Print the results
    printf("========================\n");
    printf("Dice Face\tFrequency\n");
    printf("========================\n");
    for (i = 0; i < 6; i++) {
        printf("%d\t\t%d\n", i + 1, dice[i]);
    }

    return 0;
}
