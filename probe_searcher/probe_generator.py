import functions as fun
import parameters as pm

input = "AtCgUUua"  # RNA/DNA sequence
input = input.upper()

anti_input = fun.anti_sequence(input)

probe_list = fun.probe_searcher(anti_input, pm.probe_length, pm.probe_num)

probe_list_odd = []
probe_list_even = []

for i in range(len(probe_list)):
    if i % 2 == 0:
        probe_list_odd.append(probe_list[i])
    else:
        probe_list_even.append(probe_list[i])

print(probe_list_odd, probe_list_even)