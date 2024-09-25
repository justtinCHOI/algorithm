#include <stdio.h>

int main() {
    int arr[100], n, pos, i;

    // Input array size
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    // Input array elements
    for (i = 0; i < n; i++) {
        printf("Enter element %d: ", i);
        scanf("%d", &arr[i]);
    }

    // Input position to delete
    printf("Enter the position to delete: ");
    scanf("%d", &pos);

    // Delete element from the array
    for (i = pos; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }
    n--; // Decrease the array size

    // Print the new array
    printf("Updated array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
