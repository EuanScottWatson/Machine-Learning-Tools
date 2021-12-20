import numpy as np


NUMBER_OF_LABELS = 3


def confusion_accuracy(confusion_matrix):
  if np.sum(confusion_matrix) > 0:
    return np.sum(np.diag(confusion_matrix)) / np.sum(confusion_matrix) * 100
  else:
    return 0.

def recall(confusion_matrix):
  # Out of all instances that are actually positive, how many are correctly retrieved?
  recall_vals = np.zeros((NUMBER_OF_LABELS, ))
  for entry in range(confusion_matrix.shape[0]):
    sum = np.sum(confusion_matrix[entry, :])
    if sum > 0:
      recall_vals[entry] = confusion_matrix[entry, entry] / sum
  
  return recall_vals, np.mean(recall_vals) if len(recall_vals) > 0 else 0

def precision(confusion_matrix):
  # Out of all instances predicted as positive, how many are correctly predicted?
  precision_vals = np.zeros((NUMBER_OF_LABELS, ))
  for entry in range(confusion_matrix.shape[0]):
    sum = np.sum(confusion_matrix[:, entry])
    if sum > 0:
      precision_vals[entry] = confusion_matrix[entry, entry] / sum
  
  return precision_vals, np.mean(precision_vals) if len(precision_vals) > 0 else 0

def f1(confusion_matrix):
  precision_vals, _ = precision(confusion_matrix)
  recall_vals, _ = recall(confusion_matrix)
  
  f1_vals = np.array([2 * p * r / (p + r) for (p, r) in zip(precision_vals, recall_vals)])
  return f1_vals, np.mean(f1_vals) if len(f1_vals) > 0 else 0


if __name__ == "__main__":
    # Add a confusion matrix with the columns being actual and rows being predicted
    # Remember to change constant at start of file with number of classes
    cm = np.array([
        [6, 2, 2],
        [1, 4, 1],
        [1, 1, 4]
    ])

    print("Accuracy: ", confusion_accuracy(cm))

    # Outputs the data in the form of: 
    # ([value for each class], macro value)
    print("Precision", precision(cm))
    print("Recall", recall(cm))
    print("F1", f1(cm))
