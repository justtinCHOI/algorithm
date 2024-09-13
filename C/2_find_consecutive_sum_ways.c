#include <stdio.h>

int solution(int n) {
    int answer = 0;
    int k = 1;

    while(k * (k - 1) / 2 < n){
        int kx = n - k * (k - 1) / 2;
        if(kx % k == 0){
            answer ++;
        }
    }
    return answer;
}

int main() {
    int n = 15;
    printf("The number of ways to represent %d as consecutive sums: %d\n", n, solution(n));
    return 0;
}
