
#! /bin/bash

# Usage in terminal : bash scripts/call_code.sh

# Be sure to be in the right directory (CP2-project-2) !!!

D=2
N=100
beta=0.43
b=0.01
seed=678
N_config=1000
config_type='h'
R=500

./ising $D $N $beta $b $seed $N_config $config_type $R
