import numpy as np
from sklearn.linear_model import Perceptron

# The 4 reviews from the first country: (taka count, bruk count)
# Labels: 1 = happy, 0 = angry
features = np.array([[3, 0], [0, 3], [2, 1], [1, 2]])
labels = np.array([1, 0, 1, 0])

model = Perceptron()
model.fit(features, labels)
print("sklearn weights:", model.coef_)
print("sklearn bias:", model.intercept_)
print("sklearn predictions:", model.predict(features))
print("New review 'Taka bruk taka taka!':", model.predict([[3, 1]]))
