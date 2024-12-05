#include <stdio.h>

int main() {
    int num1, num2, product;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    product = num1 * num2;

    printf("Product of %d and %d is %d\n", num1, num2, product);

    return 0;
}