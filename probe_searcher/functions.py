import random as rd

def anti_sequence(input):
    output = ""
    for i in range(len(input)):
        letter_in = input[i]
        if letter_in == "A":
            letter_out = "T"
        elif letter_in in ["T", "U"]:
            letter_out = "A"
        elif letter_in == "G":
            letter_out = "C"
        elif letter_in == "C":
            letter_out = "G"
        elif letter_in == "U":
            letter_out = "A"
        output = output + letter_out
    return output


# def probe_searcher(input, length, num):
#     probe_list = []
#     input_length = len(input)
#     area_length = input_length // num
#     for i in range(num):
#         start = area_length * i
#         probe = input[start: start + length]
#         probe_list.append(probe)
#     return probe_list


def probe_searcher(input, length, num, space):
    num_left = num
    probe_list = []
    input_temp = input
    while num_left != 0:
        probe_list.append(input_temp[0:length])
        input_temp = input_temp[length + space:]
        num_left -= 1
    return probe_list


def CG_calculator(input):
    length_input = len(input)
    CG_num = 0
    for i in range(length_input):
        if input[i] in ["C", "G"]:
            CG_num += 1
    return int(round(CG_num / length_input, 2) * 100)


def probe_searcher_CG(input, length, num, space, CG_min, CG_max):
    num_left = num
    probe_list = []
    input_temp = input
    while num_left != 0:
        for i in range(len(input_temp) - length):
            probe = input_temp[i: i + length]
            CG_ratio = CG_calculator(probe)
            if CG_ratio >= CG_min & CG_ratio <= CG_max:
                input_temp = input_temp[length + space:]
                num_left -= 1
                probe_list.append(probe)
                break
    return probe_list


def probe_searcher_infinite(input, length, space, CG_min, CG_max):
    probe_list = []
    input_temp = input
    while True:
        for i in range(len(input_temp) - length):
            probe = input_temp[i: i + length]
            CG_ratio = CG_calculator(probe)
            if CG_ratio >= CG_min & CG_ratio <= CG_max:
                input_temp = input_temp[length + space:]
                probe_list.append(probe)
                break
            if len(input_temp) < length:
                break
        if len(input_temp) < length:
            break
    return probe_list


def random_probe_generator(length, num, CG_min, CG_max):
    probe_list = []
    while num != 0:
        probe = ""
        for i in range(length):
            probe += rd.choice(["A", "T", "G", "C"])
        CG_ratio = CG_calculator(probe)
        if CG_ratio >= CG_min & CG_ratio <= CG_max:
            probe_list.append(probe)
            num -= 1
    return probe_list
