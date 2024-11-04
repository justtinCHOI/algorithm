#include <stdio.h>
#include <string.h>

void remove_vowels(char *str) {
    int i, j = 0;
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u' &&
            str[i] != 'A' && str[i] != 'E' && str[i] != 'I' && str[i] != 'O' && str[i] != 'U') {
            str[j++] = str[i];
            }
    }
    str[j] = '\0';
}

int main() {
    char str[100];
    printf("텍스트를 입력하시오 : ");
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = '\0';
    remove_vowels(str);
    printf("최종 텍스트 : %s\n", str);
    return 0;
}
