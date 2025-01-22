#include <setup.h>
#include <tuple>

tuple<vector<vector<int>>, double> metropolis(int D, int N, float beta, float b, int seed, int N_config, function<vector<vector<int>>(int, int)> config_type);

int replica_method(int D, int N, float beta, float b, int N_config, function<vector<vector<int>>(int, int)> config_type);