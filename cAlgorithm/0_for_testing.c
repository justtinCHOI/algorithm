#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_palindrome(char *originalStr)
{
    int i = 0;
    int j = strlen(originalStr) - 1;
    bool is_palindrome = true;
    while (i < j)
    {
        if (originalStr[i] != originalStr[j])
        {
            is_palindrome = false;
            break;
        } else
        i++;
        j--;
    }
    return is_palindrome;

}

int main()
{
    char originalStr[100];
    printf("문자열을 입력하시오 : ");
    fgets(originalStr, 100, stdin);
    originalStr[strcspn(originalStr, "\n")] = '\0';
    if (is_palindrome(originalStr)) {
        printf("%s은 회문입니다.\n", originalStr);
    } else {
        printf("%s은 회문이 아닙니다.\n", originalStr);
    }
    return 0;

}