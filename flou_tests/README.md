# Running error and convergence tests with Flou.jl

This folder contains the Julia scripts that generate the table and plot of figure 2. The actual
solver is implemented in [this branch](https://github.com/Andres-MG/Flou.jl/tree/research/2023.1)
of Flou.jl and requires, at least, Julia v1.8.5.

## Instructions

First, move into this folder and clone the Flou.jl repository

```shell
git clone https://github.com/Andres-MG/Flou.jl.git
```

Enter the Flou.jl folder, switch to the branch with the code for the article and instantiate the
project

```shell
cd Flou.jl
git switch research/2023.1
julia --project=. -e 'import Pkg; Pkg.instantiate()'
```

Go back to this folder and install the rest of the packages

```shell
cd ..
julia --project=. -e 'import Pkg; Pkg.develop(path="./Flou.jl")'
julia --project=. -e 'import Pkg; Pkg.add(["LaTeXStrings", "OrdinaryDiffEq", "Plots", "Printf"])'
```

Execute the scripts. Use more processes (`-p [# of CPUs]`) to speed up the computations

```shell
julia --project=. -p 4 -e 'include("errors.jl")'       # Creates the files 'errors.tex' and `errors.pdf`
julia --project=. -p 4 -e 'include("convergence.jl")'  # Creates the file 'convergence.pdf'
```

