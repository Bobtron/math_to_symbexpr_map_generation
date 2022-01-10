#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int f_002(int a, int b) {
    return (int)(2 * (a - b));
}

int main(int argc, char *argv[]) {

    if (argc < 3) {
        fprintf(stderr, "usage: %s a b\n", argv[0]);
        return EXIT_FAILURE;
    }
    printf("%d\n", f_002(atoi(argv[1]), atoi(argv[2])));
    return EXIT_SUCCESS;
}
