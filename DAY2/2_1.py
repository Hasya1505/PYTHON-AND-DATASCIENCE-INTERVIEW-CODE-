# Q1. ML – Implement Logistic Regression from Scratch

# Write code to:

# Implement Logistic Regression using Gradient Descent
# No sklearn allowed
# Include:
# Sigmoid function
# Loss (Binary Cross Entropy)
# Weight update

# 👉 Bonus: Add L2 regularization


import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, epochs=1000, l2=0.0):
        self.lr = lr
        self.epochs = epochs
        self.l2 = l2

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        n, m = X.shape
        self.w = np.zeros(m)
        self.b = 0

        for _ in range(self.epochs):
            z = np.dot(X, self.w) + self.b
            y_pred = self.sigmoid(z)

            # gradients
            dw = (1/n) * np.dot(X.T, (y_pred - y)) + self.l2 * self.w
            db = (1/n) * np.sum(y_pred - y)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        return (self.sigmoid(z) > 0.5).astype(int)
