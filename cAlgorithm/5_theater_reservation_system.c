#include <stdio.h>

int main() {
    int seats[10] = {0}; // 0: 예약 안 됨, 1: 예약 됨
    char choice;
    int seat_number;

    while (1) {
        // 좌석 상태 출력
        printf("========================\n");
        for (int i = 1; i <= 10; i++) {
            printf("%d ", i);
        }
        printf("\n========================\n");
        for (int i = 0; i < 10; i++) {
            printf("%d ", seats[i]);
        }
        printf("\n");

        // 예약 여부 질문
        printf("좌석을 예약하시겠습니까? (y 또는 n): ");
        scanf(" %c", &choice);

        if (choice == 'n' || choice == 'N') {
            printf("예약을 종료합니다.\n");
            break;
        }

        // 좌석 번호 입력
        printf("몇 번째 좌석을 예약하시겠습니까? (1-10): ");
        scanf("%d", &seat_number);

        if (seat_number < 1 || seat_number > 10) {
            printf("잘못된 좌석 번호입니다. 다시 입력해주세요.\n");
            continue;
        }

        // 좌석 예약 처리
        if (seats[seat_number - 1] == 0) {
            seats[seat_number - 1] = 1;
            printf("예약되었습니다.\n");
        } else {
            printf("이미 예약된 좌석입니다. 다른 좌석을 선택해주세요.\n");
        }
    }

    return 0;
}
