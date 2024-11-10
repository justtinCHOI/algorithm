#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

int is_strong_password(const char *password) {
    bool has_upperCase = false, has_lowerCase = false, has_digitCase = false;
    for (int i = 0; password[i] != '\0'; i++) {
        if (isupper(password[i])) has_upperCase = true;
        else if (islower(password[i])) has_lowerCase = true;
        else if (isdigit(password[i])) has_digitCase = true;
    }
    return has_upperCase && has_lowerCase && has_digitCase;
}

int main() {
    char password[100];
    while (true) {
        printf("암호를 생성하시오 : ");
        fgets(password, 100, stdin);
        password[strcspn(password, "\n")] = '\0';

        if (is_strong_password(password)) {
            printf("적정한 암호입니다.\n");
            break;
        }
        printf("숫자, 소문자, 대문자를 섞어서 암호를 다시 만드세요!\n");
    }
    return 0;
}
