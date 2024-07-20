kenlm_mrr = []
kenlm_hashes = []
with open('mrr_partial.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        hash_and_mrr = line.strip().split(" ")
        kenlm_mrr.append(float(hash_and_mrr[1]))
        kenlm_hashes.append(hash_and_mrr[0])


# write the values to a file
with open('mrr_kenlm_value.txt', 'w') as f:
    for i in range(len(kenlm_mrr)):
        f.write(f'{kenlm_mrr[i]}\n')



your_model_mrr = {}
with open('node_mrr_completed_v1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        hash_and_mrr = line.strip().split(" ")
        your_model_mrr[hash_and_mrr[0]] = float(hash_and_mrr[1])

graph_model_mrr = []

for item in kenlm_hashes:
    graph_model_mrr.append(your_model_mrr[item])

with open('mrr_graph_value.txt', 'w') as f:
    for i in range(len(graph_model_mrr)):
        f.write(f'{graph_model_mrr[i]}\n')


# import matplotlib.pyplot as plt

# plt.hist(mrr_values, color="lightgreen", ec = "black", bins=20)
# plt.xlabel('MRR')
# plt.ylabel('Frequency of Test Graphs')
# plt.title('Histogram of Node Prediction MRR for Test Graphs Using KenLM')
# plt.show()


# highest_mrr = max(mrr_values)
# lowest_mrr = min(mrr_values)
# average_mrr = sum(mrr_values) / len(mrr_values)
# print("Total graphs: ", len(mrr_values))
# # how many has 0 mrr
# print("Zero MRR: ", len([mrr_value for mrr_value in mrr_values if mrr_value == 0.0]))

# # how many has 1 mrr
# print("1 MRR: ", len([mrr_value for mrr_value in mrr_values if mrr_value == 1.0]))

# # median mrr
# mrr_values.sort()
# median_mrr = mrr_values[len(mrr_values)//2]
# print("Median MRR: ", median_mrr)


# print(f'Highest MRR: {highest_mrr}')
# print(f'Lowest MRR: {lowest_mrr}')
# print(f'Average MRR: {average_mrr}')



# import pandas as pd
# df = pd.DataFrame(mrr_values, columns=['MRR'])
# print(df.describe())


# import matplotlib.pyplot as plt



# data = [kenlm_mrr, your_model_mrr]

# # Creating boxplot
# plt.boxplot(data, labels=['KenLM', 'Graph Model'])
# plt.title('Node Prediction MRR Distribution: KenLM vs. Graph Model')
# plt.xlabel('Model')
# plt.ylabel('MRR')
# plt.show()