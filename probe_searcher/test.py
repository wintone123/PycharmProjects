import functions as fun
import parameters as pm

input = "CGACGAUCGUAGCUGUACGUAGugcaugcuagcuagugcguagcuagcuagcuagcguagugcuagucguagugucguagcuagucgaugcuagucagucgaugcuagcuagcaugcu"  # RNA/DNA sequence
input = input.upper()

#print(input)
#print(fun.CG_calculator("CGACGAUCGUAGCUGUACGUAGUGCAUGCU"))
#print(fun.probe_searcher(input, 5, 5))
#print(fun.probe_searcher_CG(input, 30, 3, 0, 50, 50))
#print(fun.probe_searcher_infinite(input, 15, 5, 48, 52))
print(fun.random_probe_generator(20, 10, 45, 55))
