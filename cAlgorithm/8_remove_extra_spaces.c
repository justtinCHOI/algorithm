#include <stdio.h>
#include <string.h>
#include <ctype.h>

void remove_extra_spaces(char *str) {
    int i, j = 0;
    int len = strlen(str);
    int space_found = 0;

    for (i = 0; i < len; i++) {
        if (!isspace(str[i])) {
            str[j++] = str[i];
            space_found = 0;
        } else if (!space_found) {
            str[j++] = ' ';
            space_found = 1;
        }
    }
    if (j > 0 && str[j - 1] == ' ') {
        str[j - 1] = '\0';
    } else {
        str[j] = '\0';
    }
}

int main() {
    char str[100];
    printf("텍스트를 입력하시오 : ");
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = '\0';  // Newline 제거
    remove_extra_spaces(str);
    printf("공백이 제거된 텍스트 : %s\n", str);
    return 0;
}
