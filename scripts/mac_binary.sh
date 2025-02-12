#! /bin/bash

# Usage in terminal : bash scripts/mac_binary.sh

# Be sure to be in the right directory (CP2-project-2) !!!



clang++ --std=c++11 src/main.cpp src/setup.cpp src/functions.cpp -o ising
