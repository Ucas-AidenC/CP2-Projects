import glob

csv_files = glob.glob("/mnt/data/*.csv")
print("CSV Files:", csv_files)

import os

directory = "/mnt/data/"
files = os.listdir(directory)

print("Files in directory:", files)
