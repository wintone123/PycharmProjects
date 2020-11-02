import os, pandas as pd

path_av = "/mnt/d/1024/日韩"
dir_av = os.listdir(path_av)

df = pd.DataFrame(columns = ['name', 'size(MB)', 'code', 'code_full'])

for dir in dir_av:
    path_av_full = path_av + "/" + dir
    list_av = os.listdir(path_av_full)
    for file in list_av:
        file_full = path_av_full + "/" + file
        file_size = os.path.getsize(file_full) // 1024 // 1024
        file_code = file.split(" ")[0]
        df_temp = pd.DataFrame([[dir, file_size, file_code, file]],
                               columns = ['name', 'size(MB)', 'code', 'code_full'])
        df = df.append(df_temp)

df.to_csv(path_av + ".csv", index = False, encoding = 'utf_8_sig')
