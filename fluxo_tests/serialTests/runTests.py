#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to run Gauss and LGL shock-capturing tests with fluxo

@author: andresrueda
"""
import os
import argparse
import sys

"""
Compiles fluxo. Must be called from serialTests folder...
"""
def compileFluxo(build_dir="build_Euler",extra_options=" ", compiler=""):
    
    # Create build directory
    exec_path = os.getcwd()+"/../builds/"+build_dir
    os.system("mkdir -p "+exec_path)
    
    #Move to that directory
    os.chdir(exec_path)
    
    # Compile the code with the desired options
    print("Configuring and compiling fluxo")
    options = " -DCMAKE_BUILD_TYPE=Release "+extra_options #-DFLUXO_ENABLE_MPI=NO 
    if compiler != "":
        options += " -DCMAKE_Fortran_COMPILER=" +compiler +" "
    
    os.system("cmake ../../fluxo/ "+options+"  > std_config.out")
    os.system("make -j > std_compile.out")
    print("Done!... ")
    
    # Go back to working directory and update exec_path
    os.chdir("../../serialTests/")
    exec_path += "/bin/fluxo"
    
    return exec_path
        
##############
# MAIN PROGRAM
##############


# Check python version
######################
assert (sys.version_info.major == 3),'python>=3.0 is needed!'

# Define arguments
##################
parser = argparse.ArgumentParser(description='Tool to run Gauss shock-capturing serial tests with FLUXO (Euler equations)', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--compiler', type=str, default='', help='Fortran compiler for FLUXO. If empty, the Fortran compiler found by cmake is used.' )

args = parser.parse_args()


# Run tests
###########

print("Running Gauss SC test!")
print("######################")

exec_path = compileFluxo(build_dir="build_Gauss",extra_options="-DFLUXO_DISC_NODETYPE=GAUSS -DFLUXO_SHOCKCAPTURE=ON -DFLUXO_FV_TIMESTEP=ON -DFLUXO_FV_BLENDSURFACE=ON -DFLUXO_SHOCK_NFVSE_CORR=ON -DNFVSE_LOCAL_ALPHA=ON", compiler=args.compiler)

os.chdir("01_Gauss_subcell")

os.system(exec_path+" parameter_Blast.ini")

os.chdir("..")

print("Running LGL SC test!")
print("####################")

exec_path = compileFluxo(build_dir="build_LGL",extra_options="-DFLUXO_DISC_NODETYPE=GAUSS-LOBATTO -DFLUXO_SHOCKCAPTURE=ON -DFLUXO_FV_TIMESTEP=ON -DFLUXO_SHOCK_NFVSE_CORR=ON -DNFVSE_LOCAL_ALPHA=ON", compiler=args.compiler)

os.chdir("02_LGL_subcell")

os.system(exec_path+" parameter_Blast.ini")

os.chdir("..")
