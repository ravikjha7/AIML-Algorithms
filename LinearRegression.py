import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset.csv')

X = np.array(df.iloc[:, 0:len(df.columns) - 1])
y = np.array(df.iloc[:, -1])

X_train, X_test, y_train, y_test = train_test_split (
        X, y, test_size=0.5
)

mean_x = np.mean(X_train)
mean_y = np.mean(y_train)

n = len(X_train)

numer = 0
denom = 0

for i in range(n):
    numer += (X_train[i] - mean_x) * (y_train[i] - mean_y)
    denom += (X_train[i] - mean_x) ** 2

b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

print(b1, b0)

n = len(X_test)

mean_y = np.mean(y_test)

ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = b0 + b1 * X_test[i]
    ss_t += (y_test[i] - mean_y) ** 2
    ss_r += (y_test[i] - y_pred) ** 2

r2 = 1 - (ss_r / ss_t)
print(f'Accuracy : {r2 * 100}')