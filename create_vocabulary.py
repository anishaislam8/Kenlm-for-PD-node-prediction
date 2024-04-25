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

            '''
            Note: You will get an error in the last line because after every n-gram, there is a empty line in the arpa file
            which causes error in the split function below. It's pretty easy to fix, but I am just being lazy :')
            The vocabulary file will be created just fine, regardless of the error.
            '''

            token = line.split('\t')[1]
            with open("trained_models/kenlm_5_without_padding_full_training_set.vocab", "a") as f:
                f.write(token+"\n")