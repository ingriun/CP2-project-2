#include <setup.h>

vector<vector<int>> initialCold(int D, int N){
    vector<vector<int>> magnet(N, vector<int>(N, 1));
    return magnet;
}

vector<vector<int>>  initialHot(int D, int N){
    vector<vector<int>> magnet(N, vector<int>(N, 1));
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int random_number = rand()%11;
            int mag = 1;
            if(random_number < 5){mag = 1;
            } else{mag = -1;}
            magnet[i][j] = mag;
        }
    }
    return magnet;
}