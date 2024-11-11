#include <stdio.h>
#include <string.h>

typedef struct {
    char productName[20];  // 상품 이름
    int unitPrice;         // 상품 가격
    int stockCount;        // 재고 수량
    int totalValue;        // 총 재고액
} Inventory;

int main() {
    Inventory warehouse[5];
    int numItems, i;

    printf("추가할 상품 수를 입력하세요 (최대 5개): ");
    scanf("%d", &numItems);

    for (i = 0; i < numItems; i++) {
        printf("==================================\n");
        printf("상품의 이름: ");
        scanf("%s", warehouse[i].productName);
        printf("상품의 가격: ");
        scanf("%d", &warehouse[i].unitPrice);
        printf("상품의 개수: ");
        scanf("%d", &warehouse[i].stockCount);
        warehouse[i].totalValue = warehouse[i].unitPrice * warehouse[i].stockCount;
        printf("==================================\n");
    }

    char targetProduct[20];
    printf("검색할 상품 이름을 입력하세요: ");
    scanf("%s", targetProduct);

    for (i = 0; i < numItems; i++) {
        if (strcmp(warehouse[i].productName, targetProduct) == 0) {
            printf("==================================\n");
            printf("상품의 이름 : %s\n", warehouse[i].productName);
            printf("상품의 가격 : %d\n", warehouse[i].unitPrice);
            printf("상품의 개수 : %d\n", warehouse[i].stockCount);
            printf("총 재고액 : %d\n", warehouse[i].totalValue);
            printf("==================================\n");
            break;
        }
    }

    if (i == numItems) {
        printf("해당 상품을 찾을 수 없습니다.\n");
    }

    return 0;
}
