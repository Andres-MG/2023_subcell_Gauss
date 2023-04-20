# Running Gauss shock-capturing tests with FLUXO

## Requirements
* Fortran compiler
* HDF5 with fortran support
* CMake (minimum required version is 3.5.1)
* python (>=3) with numpy and matplotlib (for plots)

## Instructions

To run the tests, follow the instructions:

* Move to this directory and Clone the fluxo repository:
  ```
  cd fluxo_tests
  git clone git@github.com:project-fluxo/fluxo.git
  ```
* Move to the branch of fluxo were shock capturing for Gauss nodes is implemented (the branch is Gauss_SC, but we add here the exact hash of the commit used to run the tests):
  ```
  cd fluxo
  git checkout f24edef94817de2174a94ae85845f32d2e47c87e
  cd ..
  ```
* To run the tests, go to the folder `serialTests` and run the tests using the python script:
  ```
  cd serialTests
  python3 runTests.py
  ```
  The python script will compile fluxo with the necessary flags and run the tests (more information in the python script).
* To visualize the contours, you can use paraview and the paraview state file in this repository.
* To generate the plots, you can use the script GetPlots.py
    
All results were obtained with [this version of fluxo](https://github.com/project-fluxo/fluxo/tree/f24edef94817de2174a94ae85845f32d2e47c87e).
