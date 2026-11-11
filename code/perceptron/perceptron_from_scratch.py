import numpy as np

np.random.seed(0)

# The 4 reviews from the first country: (taka count, bruk count)
# Labels: 1 = happy, 0 = angry
features = np.array([[3, 0], [0, 3], [2, 1], [1, 2]])
labels = np.array([1, 0, 1, 0])


def score(weights, bias, x):
    return np.dot(weights, x) + bias


def step(s):
    return 1 if s >= 0 else 0


def prediction(weights, bias, x):
    return step(score(weights, bias, x))


def error(weights, bias, x, y):
    if prediction(weights, bias, x) == y:
        return 0
    return abs(score(weights, bias, x))


def mean_perceptron_error(weights, bias, features, labels):
    total = sum(error(weights, bias, x, y) for x, y in zip(features, labels))
    return total / len(features)


def perceptron_trick(weights, bias, x, y, learning_rate=0.01):
    pred = prediction(weights, bias, x)
    weights = weights + learning_rate * (y - pred) * x
    bias = bias + learning_rate * (y - pred)
    return weights, bias


def perceptron_algorithm(features, labels, learning_rate=0.01, epochs=200):
    weights = np.ones(features.shape[1])
    bias = 0.0
    errors = []
    for epoch in range(epochs):
        errors.append(mean_perceptron_error(weights, bias, features, labels))
        i = np.random.randint(len(features))
        weights, bias = perceptron_trick(weights, bias, features[i], labels[i], learning_rate)
    return weights, bias, errors


weights, bias, errors = perceptron_algorithm(features, labels)
print("Weights:", weights)
print("Bias:", bias)
print("Final mean error:", mean_perceptron_error(weights, bias, features, labels))
print("Predictions:", [prediction(weights, bias, x) for x in features])
