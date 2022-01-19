import pandas as pd
from zipfile import ZipFile
import csv
import glob


rows = []

with ZipFile("C:/***/**/**/**/**/-.zip", mode = 'r') as unzip:
    # return a list that contains all files inside the zipfile.
    list_file = unzip.namelist()
    print(list_file)
    #Extract files from the list
    data = unzip.extract(list_file[0], path = "C:/***/**/**/**/**/*")
    
    
the_1st_file = pd.read_csv("C:/***/**/**/**/**/-.csv", encoding="unicode_escape")

#print

the_1st_file.head()

# READ CSV USING CSV LIBRARY

with open("C:/***/**/**/**/**/-.csv", 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
        
print(header)
print(rows)

# to use the second method then use pandas dataframe

df = pd.DataFrame(rows, columns=header)

#print()
df.head()

# To read all files from a folder

the_path = r"C:/***/**/**/**/--/"

all_files = glob.glob(the_path + "/*.csv")

li = []

for file in all_files:
    files = file
    data = pd.read_csv(files, index_col=None, header=0, encoding = "unicode_escape")
    li.append(data)
    
# Concat all data in one list

frame = pd.concat(li, axis=0, ignore_index=True)

#print()
frame.head()

os.makedirs()
os.makedirs(path, exist_ok=True)
