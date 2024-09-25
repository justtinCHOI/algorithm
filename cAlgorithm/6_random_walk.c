#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

void print_tiles(int position) {
    for (int i = 0; i < SIZE; i++) {
        if (i == position) {
            printf("*");
        } else {
            printf("_");
        }
    }
    printf("\n");
}

int main() {
    srand(time(0)); // 랜덤 시드 설정
    int position = SIZE / 2; // 딱정벌레의 초기 위치 (가운데)

    for (int i = 0; i < 10; i++) {
        print_tiles(position); // 현재 위치 출력

        // -1(왼쪽), 1(오른쪽) 중 랜덤 선택
        int move = (rand() % 2 == 0) ? -1 : 1;
        position += move;

        // 경계 체크 (타일 밖으로 나가지 않게)
        if (position < 0) {
            position = 0;
        } else if (position >= SIZE) {
            position = SIZE - 1;
        }
    }

    return 0;
}
