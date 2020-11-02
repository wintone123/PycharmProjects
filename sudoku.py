mat = [1,2,3,4,5,6,7,8,9]

def mat_to_dict(mat):
    dict = {}
    for i in range(0,3):
        for j in range(0, 3):
            dict[str(i) + str(j)] = 0
    return dict