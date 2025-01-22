#include <stdbool.h>
#include <functions.h>
#include <tuple>
#include <numeric>

tuple<vector<vector<int>>, double> metropolis(int D, int N, float beta, float b, int seed, int N_config, function<vector<vector<int>>(int, int)> config_type){
    srand(seed); //set random seed
    double energy = 0.0;
    
    //initial condition
    vector<vector<int>> spin = config_type(D, N); 

    //calculate initial energy
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int jp = (j + 1) % N; //right neighbour
            int ip = (i + 1) % N; //bottom neighbour
            energy += spin[i][j]*spin[i][jp]; //horizontal contribution
            energy += spin[i][j]*spin[ip][j]; //vertical contribution
        }
    }

    //Metropolis Algorithm
    for (int n=0; n<N_config; n++){
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                //compute ΔH
                int jp = (j+1)%N; //right neighbour
                int jm = (j-1+N)%N; //left neighbour, ensuring PBCs
                int ip = (i+1)%N; //bottom neighbour
                int im = (i-1+N)%N; //top neighbour, ensuring PBCs

                int Sn = spin[i][j]; //spin at position (i,j)
                int neighbour_sum = 0; //initialise sum
                neighbour_sum += (spin[i][jp] + spin[i][jm] + spin[ip][j] + spin[im][j]);
                float deltaH = 2*beta*Sn*neighbour_sum + 2*b*Sn;

                //generate random number in [0,1]
                float r = static_cast<float>(rand()) / RAND_MAX;

                //accept or reject new configuration
                if (exp(-deltaH)>r) {
                    spin[i][j] = -Sn; //flip spin
                }
            }
        }
    }

    //return final spin config and energy as a tuple
    return {spin, energy};
}

int replica_method(int D, int N, float beta, float b, int N_config, function<vector<vector<int>>(int, int)> config_type = initialHot, int R = 500){
    vector<int> magnetisation(R, 0);
    vector<int> energies(R, 0);

    for (int r = 0; r < R; r ++){
        int seed = time(NULL);
        //call metropolis algorithm for each step
        auto [spin, energy] = metropolis(D, N, beta, b, seed, N_config, config_type);
        auto total_spin = accumulate(spin.begin(), spin.end(), 0);
        magnetisation[r] = total_spin;
        energies[r] = energy;
    }


}