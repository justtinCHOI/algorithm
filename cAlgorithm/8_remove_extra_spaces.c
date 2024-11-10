#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

void remove_extra_spaces(char *orgStr, char *newStr) {
    int i, j = 0;
    int len = strlen(orgStr);
    bool space_detected_in_previous_char = false;

    for (i = 0; i < len; i++) {
        if (!isspace(orgStr[i])) {
            newStr[j++] = orgStr[i];
            space_detected_in_previous_char = false;
        } else if (!space_detected_in_previous_char) {
            newStr[j++] = ' ';
            space_detected_in_previous_char = true;
        }
    }
    if (j > 0 && newStr[j - 1] == ' ') {
        newStr[j - 1] = '\0';
    } else {
        newStr[j] = '\0';
    }
}

int main() {
    char orgStr[100];
    char newStr[100];
    printf("텍스트를 입력하시오 : ");
    scanf("%99[^\n]", orgStr);

    remove_extra_spaces(orgStr, newStr);
    printf("공백이 제거된 텍스트 : %s\n", newStr);
    return 0;
}
