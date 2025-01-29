#! /bin/bash

# Usage in terminal : bash script.sh

# Be sure to be in the right directory (CP2-project-2) !!!



# if 'ising' not present in the project, write either :

# Linux : g++ main.cpp setup.cpp functions.cpp -o ising
# Mac : clang++ main.cpp setup.cpp functions.cpp -o ising


D=2
N=100
beta=0.43
b=0.01
seed=28
N_config=1000
config_type='c'

./ising $D $N $beta $b $seed $N_config $config_type