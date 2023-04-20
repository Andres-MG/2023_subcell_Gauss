import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

########################################################################################################################
# Fluxo DATA 

Gauss = np.genfromtxt("serialTests/01_Gauss_subcell/out.NAVIERSTOKES_BLAST.dat", skip_header=2, delimiter=",", names=True,invalid_raise=False)
LGL = np.genfromtxt("serialTests/02_LGL_subcell/out.NAVIERSTOKES_BLAST.dat", skip_header=2, delimiter=",", names=True,invalid_raise=False)
###########################################################################

var = "alpha_amount"
plt.plot(Gauss['t_sim'],Gauss[var],label="Gauss (CFL=0.9)")
#plt.plot(Gauss_lowCFL['t_sim'],Gauss_lowCFL[var],label="Gauss (CFL=0.45)")
plt.plot(LGL['t_sim'],LGL[var],label="LGL (CFL=0.9)")

plt.xlabel("t")
plt.ylabel("$\\bar \\alpha$")
plt.xlim([0,1])
plt.legend()

###########################################################################
plt.figure()
var = "timesteps"
plt.plot(Gauss['t_sim'],Gauss[var],label="Gauss (CFL=0.9)")
#plt.plot(Gauss_lowCFL['t_sim'],Gauss_lowCFL[var],label="Gauss (CFL=0.45)")
plt.plot(LGL['t_sim'],LGL[var],label="LGL (CFL=0.9)")

plt.xlabel("t")
plt.ylabel("Time steps")
plt.xlim([0,1])
plt.legend()

