import matplotlib.pyplot as plt
import numpy as np



monitors = ["X-", "X+",
           "Y-", "Y+",
           "Z-", "Z+"]

PART2_DATAPATH = "./data_wassim/part2perfcondq5_"


debug = False



#amp phase amp phase .......

def GetData(file_path):
    file = open(file_path).read()
    data = file.splitlines()[4:]
    data = [[float(x) for x in i.split()] for i in data]
    return data

def ExtractValues(data):
    # Create amp and phase 
    amp = [[line[i] for i in range(len(line)) if i%2 == 0] for line in data]
    phase = [[line[i] for i in range(len(line)) if (i+1)%2 == 0] for line in data]
    return {"amp": amp, "phase": phase}


def ShowMatrix(mat):
    plt.imshow(mat, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()



def Extract(path):    
    data = GetData(path)
    return ExtractValues(data)

#Get data for all components
def GetComplexFields(monitor, prefix):
    E, H, ex, ex ,ez, hx, hy, hz = None,  None,  None,  None,  None,  None, None, None



    try:
        ex = Extract(f'{prefix}{monitor}_f1_ex.dat')
        ey = Extract(f'{prefix}{monitor}_f1_ey.dat')
        ez = Extract(f'{prefix}{monitor}_f1_ez.dat')
    except:
        if debug: print("E not available")

    try:
        hx = Extract(f'{prefix}{monitor}_f1_hx.dat')
        hy = Extract(f'{prefix}{monitor}_f1_hy.dat')
        hz = Extract(f'{prefix}{monitor}_f1_hz.dat')
    except:
        if debug: print("H not available")

    E = np.zeros((len(ex["amp"]), len(ex["amp"][0]),3), dtype=np.complex128)

    if hx != None: H = np.zeros((len(hx["amp"]), len(hx["amp"][0]),3), dtype=np.complex128)


    # Z0 = np.sqrt(4*np.pi*1e-7 / (1/(36*np.pi*1e-7)))*1e-6

    for x in range(len(ex["amp"])):
        for y in range(len(ex["amp"][0])):
            E[x, y] = np.array([ex["amp"][x][y] * np.exp(1j*(ex["phase"][x][y]/180 *np.pi)),
                                ey["amp"][x][y] * np.exp(1j*(ey["phase"][x][y]/180 *np.pi)),
                                ez["amp"][x][y] * np.exp(1j*(ez["phase"][x][y]/180 *np.pi))])
            
            if hx != None: H[x, y] = np.array([hx["amp"][x][y] * np.exp(1j*(hx["phase"][x][y]/180 *np.pi)),
                                hy["amp"][x][y] * np.exp(1j*(hy["phase"][x][y]/180 *np.pi)),
                                hz["amp"][x][y] * np.exp(1j*(hz["phase"][x][y]/180 *np.pi))])
            
            # print(E[x, y])
            # quit()
            

    # Ds = 0.02 mu
    return E,H




              #X   Y   Z

def ComputePower(monitor, ds, prefix):
    """
    Question 1 answer, computes one monitor. need to sum on all of them to get it.
    """
    E,H = GetComplexFields(monitor, prefix)

    # Calculate Z0
    Z0 = np.sqrt(4 * np.pi * 1e-7 / (1 / (36 * np.pi * 1e-7)))
    
    # Calculate the Poynting vector (time-averaged) using complex conjugates
    PoyntingIG = 0.5 * np.cross(E, np.conj(H)).real
    
    # Calculate the dot product of Poynting vector with the surface normal vector (ds)
    # to account for the flux through that surface
    scalar_products = np.einsum('ijk,k->ij', PoyntingIG, ds)
    
    # Sum up all the contributions for this monitor/surface
    sum_flux = np.sum(scalar_products)
    
    # Compute the power passing through this surface
    power = sum_flux * np.linalg.norm(ds) / Z0 * 1e6
    
    return power # < Error in units, find out why






"""
QUESTION 1 OF PART I
"""
dss = np.array([[ -2e-9,  0,     0],   # X-
                [  2e-9,  0,     0],   # X+
                [  0,    -2e-9,  0],   # Y-
                [  0,     2e-9,  0],   # Y+
                [  0,     0,    -2e-9], # Z-
                [  0,     0,     2e-9]]) # Z+

values = [ComputePower(monitors[i], dss[i], "./data/data_1/fwtmp_") for i in range(len(monitors))]

print("I) 1, P0",np.sum(values)) # ISSUE WITH UNITS






"""
QUESTION 1 OF PART I
power of simulation data_emitter_air
"""
dss = np.array([[ -1e-9,  0,     0],   # X-
                [  1e-9,  0,     0],   # X+
                [  0,    -1e-9,  0],   # Y-
                [  0,     1e-9,  0],   # Y+
                [  0,     0,    -1e-9], # Z-
                [  0,     0,     1e-9]]) # Z+

values = [ComputePower(monitors[i], dss[i], "./data/data_emitter_air/fwtmp_01_") for i in range(len(monitors))]

P_0_in_air = np.sum(values)

print("I) 1, Using new 10nm grid, error in units : ",P_0_in_air) # ISSUE WITH UNITS



"""
QUESTION 2 OF PART I
"""

eps0 = 1e-9/36/(np.pi)
eps = 1
C = 299792458
L = 800e-9
k = 2*np.pi/L
omega = k*C
amplitude = np.sqrt((12 * np.pi * eps0 * 1 * P_0_in_air) / ( omega * k**3))

print("I) 2, Amplitude :", amplitude)


"""
QUESTION 3 OF PART I
"""

E, H = GetComplexFields("dipole", "./data/Iq4/fwtmp_")


E_max = np.max(np.abs(E[:, :, 0])).real * 1e6 # Point is on E[5, 5] => phase 8.99772E+01

phase = np.arcsin( ((2*P_0_in_air)/omega) * 1/(amplitude * E_max)     )

print( 'I) 3, Phase :',   (phase, np.pi-phase)   )



"""
QUESTION 4 PART I
"""
# print(E_max)
# amplitude = 1.13*1e-30
# print(amplitude * np.exp(-1j * phase))
# print(amplitude * np.exp(-1j * np.pi-phase))

E_angle = 8.99772E+01 * (np.pi/180)

def ComputeDipoleMoment(amplitude, phase):
    """
    Computes the two possible dipole moments based on the amplitude and phase.
    """
    # Dipole moments based on the two possible phases
    dipole_moment_1 = amplitude * np.exp(-1j * phase ) * np.exp(1j*E_angle)
    dipole_moment_2 = amplitude * np.exp(-1j * (np.pi - phase)) * np.exp(1j*E_angle)

    return dipole_moment_1, dipole_moment_2



# Example usage based on the previously computed amplitude and phase
dipole_moment_1, dipole_moment_2 = ComputeDipoleMoment(amplitude, phase)

print(f"I) 4, Dipole Moment 1: {dipole_moment_1}")
print(f"      Dipole Moment 2: {dipole_moment_2}")






"""
QUESTION 5 PART II
Justify :
Dipole is next to a metal, dipole is a + and - charge oscillating. However, next to a metal surface, so the - charge if closer to the surface leads to a + charge inside of it. Alternatively, a + charge next to the metal leads to a - charge inside. This creates a second dipole inside of the metal that is synced with the original one. Thus we have double the power P0

Add small paragraph on local density of state
"""
print(" ==== PART II ====")


monitors = ["x-", "x+",
           "y-", "y+",
           "z-", "z+"]






# E, H = GetComplexFields("moni_dipole", "./data/PEC_2_niels/fwtmp_pec_")
# E, H = GetComplexFields("dipole", "./data/perfect_conductor/fwtmp_")

E, H = GetComplexFields("center", PART2_DATAPATH)


# sum_E = np.sum(E[:,:,2].flatten())
sum_E = np.max(E[:,:,2].flatten())




E_z = sum_E


# E, H = GetComplexFields("moni_dipole", "./data/PEC_2/fwtmp_pec_")
# E_z = E[:,:,2]
# E_z = np.sum(E_z)

# Error in source file

P_1 = omega/2 * (dipole_moment_1.conjugate() * E_z).imag * 1e6
P_2 = omega/2 * (dipole_moment_2.conjugate() * E_z).imag * 1e6
print(f'II.A) 5, using p_1 : {P_1}')
print(f'       using p_2 : {P_2}')
P = max(P_1, P_2)
print(f'       Retained value => {P}')
print(f'       ------- P/(2*P0) {P/(2*P_0_in_air)*100:.2f}%')






"""
QUESTION 6 PART II
"""

gammma_total = P/P_0_in_air
print(f'II.A) 6, Total gamma : {gammma_total}')
# 1.9871



"""
QUESTION 7 PART II
import data from monitor on the side (6)
reconstruct field
smae computations than for P_0_in_air to get PRadiant

faire E .vect. H

Gamma_r = PRadiant / P_0_in_air  doit etre inférieur à gamma_total 1.9815
"""

def Compute_P(monitors):
    dss = np.array([[ -1e-9,  0,     0],   # X-
                    [  1e-9,  0,     0],   # X+
                    [  0,    -1e-9,  0],   # Y-
                    [  0,     1e-9,  0],   # Y+
                    [  0,     0,    -1e-9], # Z-
                    [  0,     0,     1e-9]]) # Z+

    values = [ComputePower(monitors[i], dss[i], PART2_DATAPATH) for i in range(len(monitors))]

    return np.sum(values)



# Wassim order
monitors = ["ozy-", "ozy+",  #
           "ozx-", "oxz+", #
            "oxy-", "oxy+"] #



P_radiant = Compute_P(monitors)

gamma_radiant = P_radiant / P_0_in_air
print(f'II.A) 7, Radiative gamma : {gamma_radiant}')


"""
QUESTION 8 PART II
"""
gamma_loss = gammma_total - gamma_radiant
# 0.0005
print(f'II.A) 8,Loss gamma : {gamma_loss}')


"""
QUESTION 9 PART II
"""

gamma_yield = 1-gamma_loss
print(f'II.A) 8, Yield gamma : {gamma_yield}')




"""
Function to compute gammas for a system===============================================================
"""




def Compute_Gammas(data_path, monitors, dipole_monitor):

    E, H = GetComplexFields(dipole_monitor, data_path)

    E_z = np.max(E[:,:,2].flatten())

    P_1 = omega/2 * (dipole_moment_1.conjugate() * E_z).imag * 1e6
    P_2 = omega/2 * (dipole_moment_2.conjugate() * E_z).imag * 1e6
    P = max(P_1, P_2)

    gammma_total = P/P_0_in_air


    def Compute_P(monitors):
        dss = np.array([[ -1e-9,  0,     0],   # X-
                        [  1e-9,  0,     0],   # X+
                        [  0,    -1e-9,  0],   # Y-
                        [  0,     1e-9,  0],   # Y+
                        [  0,     0,    -1e-9], # Z-
                        [  0,     0,     1e-9]]) # Z+

        values = [ComputePower(monitors[i], dss[i], data_path) for i in range(len(monitors))]

        return np.sum(values)




    P_radiant = Compute_P(monitors)

    gamma_radiant = P_radiant / P_0_in_air

    gamma_loss = gammma_total - gamma_radiant


    gamma_yield = 1-gamma_loss

    return {
        "total"     : gammma_total,
        "radiative" : gamma_radiant,
        "loss"      : gamma_loss,
        "yield"     : gamma_yield
    }




def PrintQuestion(dic, letter):
    print(f'II.{letter}) Total gamma : {dic["total"]}\nII.{letter}) Radiative gamma : {dic["radiative"]}\nII.{letter}) Loss gamma : {dic["loss"]}\nII.{letter}) Yield gamma : {dic["yield"]}\n')




def wrapper(data_path, monitors, dipole_monitor, letter):
    PrintQuestion(Compute_Gammas(data_path, monitors, dipole_monitor), letter)



monitors = ["X-", "X+",
           "Y-", "Y+",
           "Z-", "Z+"]

# Niels
niels_monitors = ["x-", "x+",
           "y-", "y+",
           "z-", "z+"]

#ashar
ashar_monitors = ["-x", "+x",
           "-y", "+y",
           "-z", "+z"]

monitors = ashar_monitors
# dipole_monitor = "dipole"
# dipole_monitor = "moni_dipole"
dipole_monitor = "at_dipole_+x"

print()
# wrapper("./data_niels/data/gold/fwtmp_gold_", monitors, dipole_monitor, "B")
# wrapper("./data_niels/data/one_gold/fwtmp_gold_1_", monitors, dipole_monitor, "C")
# wrapper("./data_niels/data/two_gold/fwtmp_gold_2_", monitors, dipole_monitor, "D")




# wrapper("./data_ashar/gold_m/box_", monitors, dipole_monitor, "B")
# wrapper("./data_ashar/one_gold/box_", monitors, dipole_monitor, "C")
# wrapper("./data_ashar/two_gold/box_", monitors, dipole_monitor, "D")




