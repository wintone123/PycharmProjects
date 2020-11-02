def tilesequence(chrom, start, end, binsize):
    start_array = np.arange(start, end, binsize)
    end_array = start_array + binsize
    if end_array[-1] > end :
        end_array[-1] = end
    out = pd.DataFrame()
    out["chrom"] = [chrom] * len(start_array)
    out["start"] = start_array
    out["end"] = end_array
    return out

def tilesequence(start, end, binsize):
    start_array = np.arange(start, end, binsize)
    end_array = start_array + binsize
    if end_array[-1] > end :
        end_array[-1] = end
    out = pd.DataFrame()
    out["start"] = start_array
    out["end"] = end_array
    return out

def overlap(a, b):
    start = a["start"]
    end = a["end"]
    score = np.array([0] * len(a))
    for i in range(0,len(b)):
        start_test = b.loc[i, "start"]
        end_test = b.loc[i, "end"]
        index_up = (np.where((start_test > start) == True))[0][-1]
        index_down = (np.where((end_test > end) == False))[0][0]
        score[index_up:index_down+1] += 1
    a["score"] = score
    return a

def inRange(data, range):
    n = 0
    if data[0] in range or data[1] in range:
        n = 1
    return n

def overlap(position, dataset):
    po = list(np.arange(position[0], position[1]))
    score = dataset.apply(inRange, axis = 1, range = po)
    return sum(score)