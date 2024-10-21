# KenLM for Node Prediction of a Pure Data File (Graph)

In this project, we evaluate a KenLM model for predicting the nodes within a Pure Data (PD) graph. The dataset used for this project can be accessed via the following links:
- https://archive.org/details/Opening_the_Valve_on_Pure_Data
- https://doi.org/10.5281/zenodo.10576757

To train and test with the KenLM model, ensure that the `database.db` file is placed in the root directory of this project.

**When you clone this repository make sure to use the *--recursive* flag to ensure the KenLM submodule is also added. For example: *git clone --recursive https://github.com/anishaislam8/Kenlm-for-next-token-prediction.git***


## Step 1: Extracting paths from our PD graphs

Since KenLM is a sequential model and the structure of PD files resembles a directed graph, we extract paths from the PD graphs by analyzing their connections (edges). This can be done using the following command:

- `mkdir paths_all`
- `python3 1.extract_paths.py train_test_hashes/model_1/train_hashes.txt database.db`

The script `1.extract_paths.py` uses the PD database (`database.db`) to extract paths from all PD graphs in the training set. The file `train_hashes.txt` contains the SHA-256 hash IDs of all parsed training PD files. You can use any of the five provided training splits. The command to run the script essentially looks like this: `python3 1.extract_paths.py <train_hash_file_location> <database_location>`. Once executed, the extracted paths are saved in the `paths_all` directory.

## Step 2: Create a training corpus
After extracting the paths from the PD graphs, we create our training corpus by merging all the paths generated from the graphs into a single file. This can be done by running the following command:
- `mkdir trained_models`
- `python3 2.create_training_data.py train_test_hashes/model_1/train_hashes.txt`

This script accesses the `paths_all` directory and merges all the paths into one file, which will be used in the subsequent stages. The resulting corpus will be saved as `corpus.txt` in the `trained_models` directory.

## Step 3: Training the KenLM model and creating the .arpa file
We can train the KenLM model on the generated corpus and produce an `.arpa` file containing the extracted *n*-grams. To install the required libraries for KenLM and its Python module, run the following commands:
- `sudo apt-get install libboost-all-dev libeigen3-dev`
- `sudo apt-get install build-essential libboost-all-dev cmake zlib1g-dev libbz2-dev liblzma-dev`
- `cd kenlm`
- `mkdir build`
- `cd build` 
- `cmake ..`
- `make -j 4`
- `pip install https://github.com/kpu/kenlm/archive/master.zip`

Resource: https://medium.com/tekraze/install-kenlm-binaries-on-ubuntu-language-model-inference-tool-33507000f33

After installing the KenLM dependencies, you can create a KenLM model of order 3 (or your preferred order by replacing the value after the `-o` flag) using your corpus by running the following command from the build directory:
- `bin/lmplz -o 3 <../../trained_models/corpus.txt >../../trained_models/kenlm_3.arpa`

This command will generate a KenLM 3-gram model trained on your corpus and save it in the `trained_models` directory as `kenlm_3.arpa`. We have also included a sample `.arpa` file in the `sample_trained_models` directory, trained on our dataset, named `kenlm_3_paths_all_not_padded.arpa`.

Please note that both the KenLM dependencies and the KenLM Python module need to be installed. The Python module is required for evaluating the model in the next step, while the KenLM dependencies are necessary to run the KenLM model, as provided by the authors, to generate the trained model (`.arpa` file).

## Step 4: Create vocabulary

To evaluate the performance of our KenLM model, we first need to create a vocabulary file that represents all the unique tokens in our corpus. You can generate the vocabulary file by running the following script:
- `python3 4.create_vocabulary.py trained_models/kenlm_3.arpa`

This script uses the trained model from step 3 and generates a vocabulary file in the `trained_models` directory titled `kenlm_vocab.vocab`. The command essentially looks like this: `python3 4.create_vocabulary.py <trained_model_location>`. We have provided a sample vocab file generated from our corpus in the `sample_trained_models` directory titled `kenlm_all_paths_without_padding.vocab`.

## Step 5: Evaluate the KenLM model

To evaluate the KenLM model's performance on the test hashes of the PD graphs in your test set, run the following command:
- `mkdir output`
- `python3 5.calculate_mrr.py trained_models/kenlm_3.arpa trained_models/kenlm_vocab.vocab database.db train_test_hashes/model_1/test_hashes_filtered.txt`

This script uses the test hashes of the PD graphs, the trained model, and the vocabulary file to calculate the mean reciprocal rank (MRR) of the PD test graphs. The command looks like this: `python3 5.calculate_mrr.py <trained_model_location> <vocab_file_location> <database_location> <test_hashes_file_location>`. You can also use our sample trained model and vocabulary, or choose any of the five test hashes from the `train_test_hashes` directory by updating the file paths in the command. The MRR values will be saved in a `mrr.txt` file after completion. And the detailed output for each node will be saved in the `output` directory where one file will be generated for each test hash.


## Optional: Run tests

We have provided sample tests for the path generation and heap stages. To run the tests, you can use the following commands:

- `python3 tests/test_extract_paths.py`
- `python3 tests/test_heap.py`