#include <stdio.h>
#include <limits.h>
#include <gmp.h>

// gcc p53.c -o p53 -lgmp 
#define N 100

void factorial(mpz_t ans, int n) {
    int i;
    mpz_init_set_ui(ans,1);

    for (i=1; i <= n; i++) {
        mpz_mul_ui(ans, ans, i);
    }
    
}

void choose(mpz_t ans, int n, int r) {
    factorial(ans, n);

    mpz_t smaller;
    factorial(smaller, r);

    mpz_t third;
    factorial(third, n-r);

    /* gmp_printf("smaller is: %Zd\n", smaller); */
    /* gmp_printf("third is: %Zd\n", third); */
    mpz_mul(smaller, smaller, third);
    /* gmp_printf("top is: %Zd\n", ans); */
    /* gmp_printf("smaller is: %Zd\n", smaller); */
    mpz_divexact(ans, ans, smaller);
}



int main(void) {
    printf("Starting.\n");
    int count = 0;
    int n=0;
    int r=0;
    /* printf("upper int limit %d\n", INT_MAX); */
    /* printf("factorial(23) %d\n", factorial(23)); */
    /* printf("choose(23, 10) %d\n", choose(23,10)); */

    for(n=1; n <= N; n++) {
        for(r=0; r <= n; r++) {
        /* for(r=0; r <= n/2 + 1; r++) { */
            /* printf("%d choose %d\n", n, r); */
            mpz_t ans;
            choose(ans, n, r);
            gmp_printf("%d choose %d is %Zd\n", n, r, ans);
            if (mpz_cmp_ui(ans , 1000000) > 0) {
                count++;
            }
        }
    }

    printf("Answer %d\n", count);

    return 0;
}
