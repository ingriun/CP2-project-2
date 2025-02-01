#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>
#include "setup.h"
#include "functions.h"
#include <iostream>
#include <vector>

int main(int argc, char** argv) {

    if (argc != 8){
        cout << "Error : number of arguments should be 7! \n";
        cout << "Usage: ./ising D N beta b seed N_config config_type=['c'|'h']";
    }
    else {
        // Initialize the input variables (using script.sh)
        int D = atoi(argv[1]);
        int N = atoi(argv[2]);
        float beta = atof(argv[3]);
        float b = atof(argv[4]);
        int seed = atoi(argv[5]);
        int N_config = atoi(argv[6]);
        char config_type = argv[7][0];

        // Call metropolis & save the outputs in 'spin' & 'energy'
        auto result = metropolis(D, N, beta, b, seed, N_config, config_type);
    }

    return 0;
}
