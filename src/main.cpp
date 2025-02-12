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

    if (argc != 9){
        cout << "Error : number of arguments should be 8! \n";
        cout << "Usage: ./ising D N beta b seed N_config config_type=['c'|'h']";
    }
    else {
        // Initialize the input variables (using script.sh)
        int D = atoi(argv[1]);
        cout << "D = " << D << " ; ";
        int N = atoi(argv[2]);
        cout << "N = " << N << " ; ";
        float beta = atof(argv[3]);
        cout << "beta = " << beta << " ; ";
        float b = atof(argv[4]);
        cout << "b = " << b << " ; ";
        int seed = atoi(argv[5]);
        cout << "seed = " << seed << " ; ";
        int N_config = atoi(argv[6]);
        cout << "N_config = " << N_config << " ; ";
        char config_type = argv[7][0];
        cout << "config_type = " << config_type << " ; ";  
        int R = atoi(argv[8]);
        cout << "R = " << R << " ; ";

        // Create output files
        output_metropolis();

        // Call metropolis & save the outputs in 'spin' & 'energy'
        auto result =  varying_b_beta(D, N, N_config, config_type, R);
    }

    return 0;
}
