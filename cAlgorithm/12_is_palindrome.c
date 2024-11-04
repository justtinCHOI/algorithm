#include <stdio.h>
#include <string.h>

int is_palindrome(const char *str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char str[100];
    printf("문자열을 입력하시오 : ");
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = '\0';

    if (is_palindrome(str)) {
        printf("%s은 회문입니다.\n", str);
    } else {
        printf("%s은 회문이 아닙니다.\n", str);
    }
    return 0;
}
