import os, glob
import pandas as pd
import time
from datetime import datetime

def total(path):
    all_files = glob.glob(os.path.join(path, "*.csv"))
    all_df = []
    for f in all_files:
        df = pd.read_csv(f, sep=',')
        df['file'] = f.split('/')[-1]
        all_df.append(df)
    merged_df = pd.concat(all_df, ignore_index=True, sort=True)
    merged_df.reset_index(inplace=True, drop=True)
    outpath = "C:/path"
    filename = 'TOTAL'+".csv"
    merged_df.to_csv(outpath + filename)
