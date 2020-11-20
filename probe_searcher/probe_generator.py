import functions as fun
import parameters as pm

input = "CGACGAUCGUAGCUGUACGUAGugcaugcuagcuagugcguagcuagcuagcuagcguagugcuagucguagugucguagcuagucgaugcuagucagucgaugcuagcuagcaugcu"  # RNA/DNA sequence
input = input.upper()



anti_input = fun.anti_sequence(input)

if pm.CG_ratio == False:
    probe_list = fun.probe_searcher(anti_input, pm.probe_length, pm.probe_num, pm.space)
else:
    probe_list = fun.probe_searcher_CG(anti_input, pm.probe_length, pm.probe_num, pm.space, pm.CG_min, pm.CG_max)

probe_list_odd = []
probe_list_even = []

if pm.probe_separation:
    for i in range(len(probe_list)):
        if i % 2 == 0:
            probe_list_odd.append(probe_list[i])
        else:
            probe_list_even.append(probe_list[i])
    print(probe_list_odd, probe_list_even)
else:
    print(probe_list)
