padding = 5

''' create the corpus file '''


with open("data/train_data_subset.txt", "r") as f:
      lines = f.readlines()
      for line in lines:
        line = line.strip()
        train_data = line
        #train_data = "START " * padding + line + " END" * padding

        # write data to a file called testcorpus
        with open("testcorpus_subset_without_padding", "a") as f:
              f.write(train_data+"\n")