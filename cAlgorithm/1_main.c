#include <stdio.h>

int main(void)
{
    int a[] = { 10, 20, 30, 40, 50 };
    int* p;
    int v;

    p = a;

    printf("a[0]=%d a[1]=%d a[2]=%d \n", a[0], a[1], a[2]);
    printf("p[0]=%d p[1]=%d p[2]=%d \n\n", p[0], p[1], p[2]);

    printf("before assignment p = %u\n", p);

    v = *p++; // p가 가르키는 값을 v에 대입 -> p 증가
    printf("after first assignment p = %u, v = %d\n", p, v);

    v = (*p)++; // p가 가르키는 값을 v에 대입 -> v 대입 -> 가르키는 값 증가
    printf("after second assignment p = %u, v = %d\n", p, v);

    v = *++p; // p 증가 -> p가 가르키는 값을 v에 대입
    printf("after third assignment p = %u, v = %d\n", p, v);

    v = ++*p; // p가 가르키는 값 증가 -> v에 대입
    printf("after forth assignment p = %u, v = %d\n", p, v);

    v = (*++p)++; // p 증가 -> p가 가르키는 값을 v에 대입 -> 가르키는 값 증가
    printf("after fifth assignment p = %u, v = %d\n", p, v);

    printf("a[0]=%d a[1]=%d a[2]=%d a[3]=%d \n", a[0], a[1], a[2], a[3]);

    return 0;
}
