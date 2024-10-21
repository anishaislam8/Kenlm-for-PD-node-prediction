# Variables
TRAIN_HASHES=train_test_hashes/model_1/train_hashes.txt
DB=database.db
CORPUS=trained_models/corpus.txt
KENLM_DIR=kenlm
KENLM_BUILD=$(KENLM_DIR)/build
MODEL=trained_models/kenlm_3.arpa
VOCAB=trained_models/kenlm_vocab.vocab
TEST_HASHES=train_test_hashes/model_1/test_hashes_filtered.txt
OUTPUT_DIR=output

# Default target
all: paths corpus kenlm_model vocabulary mrr

# Step 1: Extracting paths from PD graphs
paths: 1.extract_paths.py	$(TRAIN_HASHES)	$(DB)
	mkdir -p paths_all
	python3 1.extract_paths.py $(TRAIN_HASHES) $(DB)

# Step 2: Create a training corpus
corpus: 2.create_training_data.py $(TRAIN_HASHES)
	mkdir -p trained_models
	python3 2.create_training_data.py $(TRAIN_HASHES)

# Step 3: Install Necessary Dependencies and Train the KenLM model
kenlm_model: $(CORPUS)
	sudo apt-get install -y libboost-all-dev libeigen3-dev build-essential cmake zlib1g-dev libbz2-dev liblzma-dev
	mkdir -p $(KENLM_BUILD)
	cd $(KENLM_BUILD) && cmake .. && make -j 4
	pip install https://github.com/kpu/kenlm/archive/master.zip
	$(KENLM_BUILD)/bin/lmplz -o 3 < $(CORPUS) > $(MODEL)

# Step 4: Create vocabulary
vocabulary: $(MODEL)	4.create_vocabulary.py
	python3 4.create_vocabulary.py $(MODEL)

# Step 5: Evaluate the KenLM model
mrr: 5.calculate_mrr.py	$(MODEL) $(VOCAB) $(TEST_HASHES) $(DB)
	mkdir -p $(OUTPUT_DIR)
	python3 5.calculate_mrr.py $(MODEL) $(VOCAB) $(DB) $(TEST_HASHES)

# Optional: Run tests
test:
	python3 tests/test_extract_paths.py
	python3 tests/test_heap.py

# Clean all generated files
clean:
	rm -rf paths_all trained_models $(KENLM_BUILD) $(OUTPUT_DIR)
