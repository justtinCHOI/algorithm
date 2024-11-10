#include <stdio.h>
#include <string.h>
#include <ctype.h>

void trim_left(char orgiStr[], char trimStr[]) {
    int i = 0, j = 0;
    int strLength = strlen(orgiStr);

    while (isspace(orgiStr[i])) {
        i++;
    }

    for (;i < strLength; i++) {
        trimStr[j++] = orgiStr[i];
    }

    trimStr[j] = '\0';
}

int main() {
    char orgiStr[100];
    char trimStr[100];
    printf("문자열을 입력하시오 : ");
    fgets(orgiStr, 100, stdin);
    orgiStr[strcspn(orgiStr, "\n")] = '\0';
    trim_left(orgiStr, trimStr);
    printf("왼쪽 공백이 제거된 문자열 : '%s'\n", trimStr);
    return 0;
}
