#include <stdio.h>
#include <ctype.h>

int is_strong_password(const char *password) {
    int has_upper = 0, has_lower = 0, has_digit = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (isupper(password[i])) has_upper = 1;
        else if (islower(password[i])) has_lower = 1;
        else if (isdigit(password[i])) has_digit = 1;
    }
    return has_upper && has_lower && has_digit;
}

int main() {
    char password[100];
    while (1) {
        printf("암호를 생성하시오 : ");
        fgets(password, 100, stdin);
        password[strcspn(password, "\n")] = '\0';

        if (is_strong_password(password)) {
            printf("적정한 암호입니다.\n");
            break;
        } else {
            printf("숫자, 소문자, 대문자를 섞어서 암호를 다시 만드세요!\n");
        }
    }
    return 0;
}
