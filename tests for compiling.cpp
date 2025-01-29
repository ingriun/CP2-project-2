#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <random>

std::ranlux48 generator;
std::uniform_int_distribution<int> distribution(1,6);


int main(int argc, char** argv) {
    int seed=atoi(argv[1]);
    int N=atoi(argv[2]);
    generator = std::ranlux48(seed);

    for (int i=0; i<N; i++){
        int random = distribution(generator);
        printf("%d \n", random);
    }
}

