import kenlm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

def predict_next_token(model, context):
    #context_tokens = context.split(" ")
    next_token_probabilities = {}

    with open("trained_models/kenlm_5_without_padding_full_training_set.vocab", "r", encoding="utf8") as vocab_f:
        vocabulary = vocab_f.readlines()
        for candidate_word in vocabulary:
            candidate_word = candidate_word.strip()
            context_with_candidate = context + " " + candidate_word
            next_token_probabilities[candidate_word] = model.score(context_with_candidate)

    predicted_next_token = max(next_token_probabilities, key=next_token_probabilities.get)
    return predicted_next_token

def evaluate_kenlm_model(model):
      y_true = []
      y_pred = []

      with open("data/test_data_20_after_project_wise_split.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                line = line.strip()
                #line = "START " * 5 + line
                sentence_tokens = line.split(" ")

                context = ' '.join(sentence_tokens[:-1])  # Use all words except the last one as context

                true_next_word = sentence_tokens[-1]
                predicted_next_word = predict_next_token(model, context)

                y_true.append(true_next_word)
                y_pred.append(predicted_next_word)

                if i%1000 == 0:
                    print(i, true_next_word, predicted_next_word)
                i+=1

            print("y_true: ", len(y_true))
            print("y_pred: ", len(y_pred))



      accuracy = accuracy_score(y_true, y_pred)
      precision = precision_score(y_true, y_pred, average='weighted', zero_division=np.nan)
      recall = recall_score(y_true, y_pred, average='weighted', zero_division=np.nan)
      f1 = f1_score(y_true, y_pred, average='weighted', zero_division=np.nan)
      return accuracy, precision, recall, f1

model = kenlm.Model('trained_models/kenlm_5_without_padding_full_training_set.arpa')
accuracy, precision, recall, f1 = evaluate_kenlm_model(model)
print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", f1)