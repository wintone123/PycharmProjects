def anti_sequence(input):
    output = ""
    for i in range(len(input)):
        letter_in = input[i]
        if letter_in == "A":
            letter_out = "T"
        elif letter_in == "T":
            letter_out = "A"
        elif letter_in == "G":
            letter_out = "C"
        elif letter_in == "C":
            letter_out = "G"
        elif letter_in == "U":
            letter_out = "A"
        output = output + letter_out
    return output

def probe_searcher(input, length, num):
    probe_list = []
    input_length = len(input)
    area_length = input_length // num
    for i in range(num):
        start = area_length * i
        probe = input[start: start + length]
        probe_list.append(probe)
    return probe_list

def CG_ration(input):
    length_input = len(input)
    CG_num = 0
    for i in range(length_input):
        if input[i] == "C" or "G":
            CG_num += 1
    return CG_num // length_input

def probe_searcher_CG(input, length, num, CG_ratio):
    num_lift = num
    probe_list = []
    input_length = len(input)
    start = 0
    while num_lift > 0:
        