#include <setup.h>

vector<vector<int>> initialCold(int D, int N){
    vector<vector<int>> magnet(N, vector<int>(N, 1));
    return magnet;
}

vector<vector<int>>  initialHot(int D, int N){
    vector<vector<int>> spin(N, vector<int>(N, 1));
    for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                spin[i][j] = (rand()%2)*2 - 1; //randomly +1 or -1
            }
        }
    return spin;
}