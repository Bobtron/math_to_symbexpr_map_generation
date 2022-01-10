#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// p = subprocess.Popen(['gcc', '-o', out_file_name, self.c_file_name, '-lm'])
// this is to compile to binary

float f_001(float a, float b) {
    return 3.0 * a / b;
}

float f_002(float a, int b) {
    if (b) {
        return a / 2;
    } else {
        return 3.0 * a;
    }
}

float f_003(float a, float b, float c) {
    return pow(a * b, 4) + cos(c);
}

float f_004(float a, float b) {
    return 2.0 * a + b;
}

int f_005(int a, int b) {
    return (a / 5) * b;
}

float f_006(float a, float b) {
    if (a <= b) {
        return a;
    } else {
        return b;
    }
}

/****************************************/

int f_plus_001(int a) {
    return a + 5;
}

int f_plus_002(int a) {
    return a + 10;
}

int f_plus_003(int a) {
    return a + 100;
}

/****************************************/

float f_sin_001(float a) {
    return sin(a) * 2.0;
}

float f_sin_002(float a) {
    return sin(a) * 0.5;
}

float f_sin_003(float a) {
    return sin(a) * 4.0;
}

float f_sin_004(float a) {
    return sin(a) * 0.25;
}

/****************************************/

int f_divide_001(float a) {
    return a / 5;
}

int f_divide_002(float a) {
    return a / 13;
}

int f_divide_003(float a) {
    return a / 99;
}

int f_divide_004(float a) {
    return a / 10;
}

/****************************************/

int f_piecewise_001(int a) {
    if (a < 50) {
        return 0;
    }
    else {
        return a + 10;
    }
}

int f_piecewise_002(int a) {
    if (abs(a - 50) < 10) {
        return 0;
    }
    else {
        return a * 2;
    }
}

int f_piecewise_003(int a) {
    if (a % 2 == 0) {
        return a * 2;
    }
    else {
        return a + 2;
    }
}

int f_piecewise_004(int a) {
    return abs(a - 50);
}

/****************************************/

int f_collatz_001(int a){

}


int main(int argc, char *argv[]) {
    float a;

    if (argc < 3) {
        fprintf(stderr, "usage: %s a b c\n", argv[0]);
        return EXIT_FAILURE;
    }
    a = f_001(atof(argv[1]), atof(argv[2]));
    printf("%f\n", a);
    a = f_002(atof(argv[1]), (int)atof(argv[2]));
    printf("%f\n", a);
    a = f_003(atof(argv[1]), atof(argv[2]), atof(argv[3]));
    printf("%f\n", a);
    a = f_004(atof(argv[1]), atof(argv[2]));
    printf("%f\n", a);
    return EXIT_SUCCESS;
}
