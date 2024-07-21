kenlm_mrr = []
with open('kenlm_mrr_final_sorted.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        hash_and_mrr = line.strip().split(" ")
        kenlm_mrr.append(float(hash_and_mrr[1]))


# write the values to a file
with open('mrr_kenlm_value.txt', 'w') as f:
    for i in range(len(kenlm_mrr)):
        f.write(f'{kenlm_mrr[i]}\n')



graph_model_mrr = []
with open('graph_mrr_final_v1_sorted.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        hash_and_mrr = line.strip().split(" ")
        graph_model_mrr.append(float(hash_and_mrr[1]))


with open('mrr_graph_value.txt', 'w') as f:
    for i in range(len(graph_model_mrr)):
        f.write(f'{graph_model_mrr[i]}\n')


import matplotlib.pyplot as plt

plt.hist(kenlm_mrr, color="lightgreen", ec = "black", bins=20)
plt.xlabel('MRR')
plt.ylabel('Frequency of Test Graphs')
plt.title('Histogram of Node Prediction MRR for Test Graphs Using KenLM')
plt.show()


highest_mrr = max(kenlm_mrr)
lowest_mrr = min(kenlm_mrr)
average_mrr = sum(kenlm_mrr) / len(kenlm_mrr)
print("Total graphs: ", len(kenlm_mrr))
# how many has 0 mrr
print("Zero MRR: ", len([mrr_value for mrr_value in kenlm_mrr if mrr_value == 0.0]))

# how many has 1 mrr
print("1 MRR: ", len([mrr_value for mrr_value in kenlm_mrr if mrr_value == 1.0]))

# median mrr
kenlm_mrr.sort()
median_mrr = kenlm_mrr[len(kenlm_mrr)//2]
print("Median MRR: ", median_mrr)


print(f'Highest MRR: {highest_mrr}')
print(f'Lowest MRR: {lowest_mrr}')
print(f'Average MRR: {average_mrr}')



import pandas as pd
df = pd.DataFrame(kenlm_mrr, columns=['MRR'])
print(df.describe())





data = [kenlm_mrr, graph_model_mrr]

# Creating boxplot
plt.boxplot(data, labels=['KenLM', 'Graph Model'])
plt.title('Node Prediction MRR Distribution: KenLM vs. Graph Model')
plt.xlabel('Model')
plt.ylabel('MRR')
plt.show()


# # R code for wilcox test
# graph_node=read.delim(header = FALSE, file = "D:\\Masters\\Thesis\\models\\kenlm\\mrr_graph_value.txt");
# kenlm_node=read.delim(header = FALSE, file = "D:\\Masters\\Thesis\\models\\kenlm\\mrr_kenlm_value.txt");
# graph_node$V1 <- as.numeric(as.character(graph_node$V1))
# kenlm_node$V1 <- as.numeric(as.character(kenlm_node$V1))
# wilcox.test(graph_node$V1, kenlm_node$V1)