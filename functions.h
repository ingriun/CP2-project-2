#include "setup.h"
#include <utility>

void output_metropolis();

pair<vector<vector<int> >, double> metropolis(int D, int N, float beta, float b, int seed, int N_config, char config_type);

pair<vector<int>, vector<double> > replica_method(int D, int N, float beta, float b, int N_config, char config_type, int R);

int varying_b_beta(int D, int N, int N_config, char config_type, int R);