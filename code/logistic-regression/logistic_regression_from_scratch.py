import numpy as np

np.random.seed(0)

# The 4 reviews from the first country: (taka count, bruk count)
# Labels: 1 = happy, 0 = angry
features = np.array([[3, 0], [0, 3], [2, 1], [1, 2]])
labels = np.array([1, 0, 1, 0])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def score(weights, bias, x):
    return np.dot(weights, x) + bias


def prediction(weights, bias, x):
    return sigmoid(score(weights, bias, x))


def log_loss(weights, bias, x, y):
    pred = prediction(weights, bias, x)
    return -y * np.log(pred) - (1 - y) * np.log(1 - pred)


def total_log_loss(weights, bias, features, labels):
    return sum(log_loss(weights, bias, x, y) for x, y in zip(features, labels))


def logistic_trick(weights, bias, x, y, learning_rate=0.1):
    pred = prediction(weights, bias, x)
    weights = weights + learning_rate * (y - pred) * x
    bias = bias + learning_rate * (y - pred)
    return weights, bias


def logistic_regression_algorithm(features, labels, learning_rate=0.1, epochs=1000):
    weights = np.ones(features.shape[1])
    bias = 0.0
    for epoch in range(epochs):
        i = np.random.randint(len(features))
        weights, bias = logistic_trick(weights, bias, features[i], labels[i], learning_rate)
    return weights, bias


weights, bias = logistic_regression_algorithm(features, labels)
print("Weights:", weights)
print("Bias:", bias)
print("Total log loss:", total_log_loss(weights, bias, features, labels))
print("Predictions:", [round(prediction(weights, bias, x), 3) for x in features])
