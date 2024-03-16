import matplotlib.pyplot as plt

Accuracy = [0.2982,  0.344, 0.384, 0.3852, 0.3886, 0.3888,0.3888 ]
Precision = [0.30400737255660987,  0.35869840027381383, 0.39200538734827, 0.39339559836077187, 0.39959878234370694, 0.3998328753870518, 0.3998328753870518]
Recall = [0.2982, 0.344, 0.384, 0.3852, 0.3886, 0.3888, 0.3888]
F1 = [0.2505403275061106, 0.348913934297602,  0.39678806186575943, 0.39914592819317124, 0.3988831131627298, 0.3991044746799747, 0.3991044746799747]
Orders = [2,3,4,5,6, 7, 8]

plt.plot(Orders, Accuracy, label = "Accuracy")
plt.plot(Orders, Precision, label = "Precision")
plt.plot(Orders, Recall, label = "Recall")
plt.plot(Orders, F1, label = "F1")
plt.xlabel('Order')
plt.ylabel('Score')
plt.title('Scores vs N-Gram Orders for Kenlm with Modified KN Smoothing')
plt.legend()
plt.show()
