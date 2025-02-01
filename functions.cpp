#include <stdbool.h>
#include "functions.h"
#include <numeric>
#include <fstream>
#include <math.h>
using namespace std;

pair<vector<vector<int> >, double> metropolis(int D, int N, float beta, float b, int seed, int N_config, char config_type){
    srand(seed); //set random seed
    double energy = 0.0;
    vector<vector<int> > spin;
    vector<int> magnetisation(N_config, 0);
    vector<double> energies(N_config, 0);
    
    //initial condition
    if(config_type == 'h'){
        spin = initialHot(D, N); 
    }
    else if (config_type == 'c'){
        spin = initialHot(D, N); 
    }
    else{
        cout << "configuration type unknown" << endl;
    }

    //Metropolis Algorithm
    for (int n=0; n<N_config; n++){
        
        // Calculate magnetisation
        int total_spin=0;
        for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                total_spin += spin[i][j];
            }
        }
        magnetisation[n] = total_spin;

        //calculate energy
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int jp = (j + 1) % N; //right neighbour
                int ip = (i + 1) % N; //bottom neighbour
                energies[n] += spin[i][j]*spin[i][jp]; //horizontal contribution
                energies[n] += spin[i][j]*spin[ip][j]; //vertical contribution
            }
        }

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
    // Write outputs in files
    std::ofstream magnetisationfile("magnetisation.csv");
    for(int i = 0; i < magnetisation.size(); i++){
        magnetisationfile << magnetisation[i] << endl;}
    magnetisationfile.close();

    std::ofstream energyfile("energy.csv");
    for(int i = 0; i < energies.size(); i++){
        energyfile << energies[i] << endl;}
    energyfile.close();

    //return final spin config and energy as a tuple
    return make_pair(spin, energy);
}

int replica_method(int D, int N, float beta, float b, int N_config, char config_type = 'h', int R = 500){
    vector<int> magnetisation(R, 0);
    vector<double> energies(R, 0);

    for (int r = 0; r < R; r ++){
        int seed = time(NULL);
        //call metropolis algorithm for each step
        auto result = metropolis(D, N, beta, b, seed, N_config, config_type);
        auto spin = std::get<0>(result);
        auto energy = std::get<1>(result);

        //calculate total spin for given configuration
        int total_spin;
        for (const auto& row : spin) {
            for (const auto& s : row) {
                total_spin += s;
            }
        }
        //add total spin for the configuration to the magnetisattion
        magnetisation[r] = total_spin;

        //add energy to total energies
        energies[r] = energy;
    }

    /*//find the mean magnetisation
    float magn_mean = 1/R * accumulate(magnetisation.begin(), magnetisation.end(), 0);

    //find the error in magnetisation
    float temp_magnetisation = 0; //temporary variable to find the error
    for (int& element : magnetisation) {
        temp_magnetisation += pow(element - magn_mean, 2);
    }
    float magn_err = pow(1/(R*(R-1)) * temp_magnetisation, 1/2);

    //expectation value for magnetisation
    float magn_exp = magn_mean + magn_err;

    //mean energy
    double energy_mean = 1/R *  accumulate(energies.begin(), energies.end(), 0);

    //find the error in energy
    double temp_energy = 0; //temporary variable to find the error
    for (double& element : energies) {
        temp_energy += pow(element - energy_mean, 2);
    }
    double energy_err = pow(1/(R*(R-1)) * temp_energy, 1/2);

    //expectation value for energy
    double energy_exp = energy_mean + energy_err;*/
    
    //writing the result to file

    std::ofstream magnetisationfile("magnetisation.txt");
    for(int i = 0; i < magnetisation.size(); i++){
        magnetisationfile << magnetisation[i] << endl;}
    magnetisationfile.close();

    std::ofstream energyfile("energy.txt");
    for(int i = 0; i < energies.size(); i++){
        energyfile << energies[i] << endl;}
    energyfile.close();

    return 0;

}