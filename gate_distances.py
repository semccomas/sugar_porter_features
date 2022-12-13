## get gate distances as an array
## gate_EC and gate_IC shape should be : gate_EC = [(TM1 start,TM1 end), (TM7 start, TM7 end)],
## and  gate_IC = [(TM4 start, TM4 end), (TM10 start, TM10 end)]

#quick refs: GLUT5: gate_EC = [(30,37), (289,295)], gate_IC = [(136,145), (386,394)]
# GLUT1: gate_EC = [(29,37), (288,295)], gate_IC = [(137,146), (385,394)]
# PfHT: gate_EC = [(43,51), (311,318)], gate_IC = [(145,154), (409,418)]


#This is from the strings directory, will change as I develop classes

def make_gate_arr(md_uni, gate_EC, gate_IC):
    from MDAnalysis.analysis import distances
    import numpy as np

    gate_EC_dists = []
    gate_IC_dists = []

    for timestep in md_uni.trajectory:
        tm1 = md_uni.select_atoms('resid %i-%i' %(gate_EC[0][0], gate_EC[0][1])).center_of_mass()
        tm7 = md_uni.select_atoms('resid %i-%i' %(gate_EC[1][0], gate_EC[1][1])).center_of_mass()
        tm4 = md_uni.select_atoms('resid %i-%i' %(gate_IC[0][0], gate_IC[0][1])).center_of_mass()
        tm10 = md_uni.select_atoms('resid %i-%i' %(gate_IC[1][0], gate_IC[1][1])).center_of_mass()


        gate_EC_dists.append(float(distances.distance_array(tm1, tm7)))
        gate_IC_dists.append(float(distances.distance_array(tm4, tm10)))
    print("returning EC gate, IC gate dists")
    gate_EC_dists = np.array(gate_EC_dists)
    gate_IC_dists = np.array(gate_IC_dists)
    return gate_EC_dists, gate_IC_dists


