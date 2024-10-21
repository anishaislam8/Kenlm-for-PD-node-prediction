import sys

model_name = sys.argv[1]

with open(model_name, "r", encoding="utf8") as f:
    lines = f.readlines()
    found_1_grams = False

    for line in lines:
        line = line.strip()
        if line == "\\1-grams:":
            found_1_grams = True
            continue
        if line == "\\2-grams:":
            break
        if found_1_grams:

            arr = line.split('\t')
            if len(arr) > 1:
                token = arr[1]
                with open("trained_models/kenlm_vocab.vocab", "a") as f:
                    f.write(token+"\n")