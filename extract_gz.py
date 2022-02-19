import glob
import gzip
import random

import numpy as np


# find all files with data
file_list = glob.glob("data/cases_*.csv.gz")
random_files = random.sample(file_list, 20)

# read each data batch and append it to a list of batches
batches = []
for i, x in enumerate(random_files):
    print(f"Reading file {i+1}/{len(random_files)}...")
    try:
        y = np.loadtxt(gzip.GzipFile(x, "r"), skiprows=1, usecols=(7, 24), delimiter=",", dtype=str)
        batches.append(y)
    except:
        print(f"Couldn't read file: {x}")
