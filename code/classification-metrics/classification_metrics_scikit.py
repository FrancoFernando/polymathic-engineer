import numpy as np
from sklearn.metrics import (confusion_matrix, precision_score, recall_score,
                             f1_score, fbeta_score, precision_recall_curve,
                             roc_curve, roc_auc_score)

# The second fraud detector of the article: 1,000 transactions, 10 frauds
# TP 8, FN 2, FP 48, TN 942
y_true = np.array([1] * 10 + [0] * 990)
y_pred = np.array([1] * 8 + [0] * 2 + [1] * 48 + [0] * 942)

print(confusion_matrix(y_true, y_pred))  # [[942  48]
                                         #  [  2   8]]
print(confusion_matrix(y_true, y_pred, labels=[1, 0]))  # [[  8   2]
                                                        #  [ 48 942]]
print(recall_score(y_true, y_pred))     # 0.8
print(precision_score(y_true, y_pred))  # 0.14285714285714285

# The two comment filters: 100 comments, 40 abusive
# Filter 1: TP 30, FN 10, FP 5, TN 55. Filter 2: TP 35, FN 5, FP 10, TN 50
comments = np.array([1] * 40 + [0] * 60)
filter_1 = np.array([1] * 30 + [0] * 10 + [1] * 5 + [0] * 55)
filter_2 = np.array([1] * 35 + [0] * 5 + [1] * 10 + [0] * 50)

print(f1_score(comments, filter_1), f1_score(comments, filter_2))  # 0.800 0.824
print(fbeta_score(comments, filter_1, beta=0.5),
      fbeta_score(comments, filter_2, beta=0.5))  # 0.833 0.795

# The 10 transactions and their probabilities of fraud
labels = np.array([1, 0, 0, 0, 1, 0, 0, 1, 1, 1])
probabilities = np.array([0.05, 0.10, 0.15, 0.18, 0.30, 0.40, 0.60, 0.70, 0.85, 0.95])

precisions, recalls, thresholds = precision_recall_curve(labels, probabilities)
print(np.round(precisions, 3))  # [0.5 0.444 0.5 0.571 0.667 0.6 0.75 1. 1. 1. 1.]
print(recalls)                  # [1.  0.8 0.8 0.8 0.8 0.6 0.6 0.6 0.4 0.2 0. ]

fpr, tpr, thresholds = roc_curve(labels, probabilities, drop_intermediate=False)
print(fpr)  # [0.  0.  0.  0.  0.2 0.4 0.4 0.6 0.8 1.  1. ]
print(tpr)  # [0.  0.2 0.4 0.6 0.6 0.6 0.8 0.8 0.8 0.8 1. ]
print(roc_auc_score(labels, probabilities))  # 0.72
