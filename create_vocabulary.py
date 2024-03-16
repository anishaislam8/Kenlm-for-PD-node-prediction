with open("trained_models/kenlm_5_without_padding_full_training_set.arpa", "r", encoding="utf8") as f:
    lines = f.readlines()
    found_1_grams = False
    i = 0
    for line in lines:
        line = line.strip()
        if line == "\\1-grams:":
            found_1_grams = True
            continue
        if line == "\\2-grams:":
            break
        if found_1_grams:
            i+=1
            print(i)
            token = line.split('\t')[1]
            with open("trained_models/kenlm_5_without_padding_full_training_set.vocab", "a") as f:
                f.write(token+"\n")