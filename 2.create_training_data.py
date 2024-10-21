import os
import sys

folder_path = "paths_all"
train_data = []

train_hashes = sys.argv[1]


with open(train_hashes, "r") as train_hash_file:
    hashes = train_hash_file.readlines()
    for hash in hashes:
        hash = hash.strip()
        filename = hash + ".txt"
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("No connections"):
                    continue
                train_data.append(line)



file_name = open('trained_models/corpus.txt','a')
for item in train_data:
    file_name.write(item+"\n")
