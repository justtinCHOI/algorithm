#include <stdio.h>
#include <string.h>
#include <ctype.h>

void trim_left(char s[]) {
    int i = 0, j = 0;
    while (isspace(s[i])) {
        i++;
    }
    while (s[i] != '\0') {
        s[j++] = s[i++];
    }
    s[j] = '\0';
}

int main() {
    char str[100];
    printf("문자열을 입력하시오 : ");
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = '\0';
    trim_left(str);
    printf("왼쪽 공백이 제거된 문자열 : '%s'\n", str);
    return 0;
}
