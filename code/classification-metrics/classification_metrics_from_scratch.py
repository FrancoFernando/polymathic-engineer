import numpy as np

# The 10 transactions of the article: 1 = fraud, 0 = legitimate,
# and the probability of fraud the detector assigned to each one
labels = np.array([1, 0, 0, 0, 1, 0, 0, 1, 1, 1])
probabilities = np.array([0.05, 0.10, 0.15, 0.18, 0.30, 0.40, 0.60, 0.70, 0.85, 0.95])


def confusion_counts(labels, probabilities, threshold):
    flagged = probabilities >= threshold
    tp = np.sum(flagged & (labels == 1))
    fp = np.sum(flagged & (labels == 0))
    fn = np.sum(~flagged & (labels == 1))
    tn = np.sum(~flagged & (labels == 0))
    return tp, fp, fn, tn


def precision(tp, fp):
    return tp / (tp + fp) if tp + fp > 0 else float("nan")


def recall(tp, fn):
    return tp / (tp + fn)


def f_beta(p, r, beta=1.0):
    return (1 + beta**2) * p * r / (beta**2 * p + r)


for threshold in [0.2, 0.5, 0.8]:
    tp, fp, fn, tn = confusion_counts(labels, probabilities, threshold)
    p, r = precision(tp, fp), recall(tp, fn)
    print(f"threshold {threshold}: TP {tp} FP {fp} FN {fn} TN {tn}  "
          f"recall {r:.2f}  precision {p:.2f}")
# threshold 0.2: TP 4 FP 2 FN 1 TN 3  recall 0.80  precision 0.67
# threshold 0.5: TP 3 FP 1 FN 2 TN 4  recall 0.60  precision 0.75
# threshold 0.8: TP 2 FP 0 FN 3 TN 5  recall 0.40  precision 1.00


# Sweep the threshold over every probability to build the ROC curve
def roc_points(labels, probabilities):
    points = []
    # The lowest probability flags everything; each step then passes one point
    for threshold in np.sort(probabilities):
        tp, fp, fn, tn = confusion_counts(labels, probabilities, threshold)
        points.append((fp / (fp + tn), tp / (tp + fn)))  # (FPR, TPR)
    points.append((0.0, 0.0))  # a threshold above every probability flags nothing
    return points


def area_under_curve(points):
    # Sum the rectangles under the staircase, from left to right
    area = 0.0
    for (x0, y0), (x1, y1) in zip(points[1:], points[:-1]):
        area += (x1 - x0) * y0
    return area


points = roc_points(labels, probabilities)
print([(round(float(x), 1), round(float(y), 1)) for x, y in points])
# [(1.0, 1.0), (1.0, 0.8), (0.8, 0.8), (0.6, 0.8), (0.4, 0.8), (0.4, 0.6),
#  (0.2, 0.6), (0.0, 0.6), (0.0, 0.4), (0.0, 0.2), (0.0, 0.0)]
print(round(area_under_curve(points), 2))  # 0.72
