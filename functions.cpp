#include <stdbool.h>
#include <functions.h>

int metropolis(int D, int N, float beta, float b, int seed, int N_config, function<vector<vector<int>>(int, int)> config_type){
    vector<vector<int>> magnet = config_type(D, N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            
        }
    }
}

int replica_method(int D, int N, float beta, float b, int N_config, bool config_type){}