# -*- coding: utf-8 -*-
"""heart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rQzXoD36-KzXAtHGPZzS_LKsKL_J6ujN
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("heart.csv")
df

x=df.drop('target',axis=1)
y=df['target']

"""DECISION TREE"""

from sklearn.tree import DecisionTreeClassifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)


y_pred = model.predict(x_test)
print(y_pred)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""RANDOM FOREST"""

from sklearn.ensemble import RandomForestClassifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Accuracy: {accuracy:.4f}")

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"KNN Accuracy: {accuracy:.4f}")

"""LOGISTIC REGRESSION"""

from sklearn.linear_model import LogisticRegression


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.201, random_state=42)


model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Accuracy: {accuracy:.4f}")

"""SVM"""

from sklearn.svm import SVC
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = SVC()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"SVM Accuracy: {accuracy:.4f}")

import matplotlib.pyplot as plt
import numpy as np

models = ["Random Forest", "KNN", "Decision Tree", "Logistic Regression", "SVM"]
accuracies = [0.9854, 0.7317, 0.9853, 0.7971, 0.6829]  # Ensure length matches models

# Sort accuracies to determine the darkest and lightest colors
sorted_indices = np.argsort(accuracies)[::-1]  # Sort in descending order

# Assign colors: Darkest for highest accuracy, lighter for lower
colors = ['darkgreen', 'forestgreen', 'mediumseagreen', 'lightgreen', 'palegreen']
ordered_colors = [colors[i] for i in np.argsort(sorted_indices)]  # Arrange colors accordingly

plt.figure(figsize=(8, 5))
bars = plt.bar(models, accuracies, color=ordered_colors)

# Adding text labels on bars
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.02, f"{acc:.4f}",
             ha='center', color='white', fontweight='bold')

plt.xlabel("Machine Learning Models")
plt.ylabel("Accuracy Score")
plt.title("Accuracy Comparison of Different ML Models (Test Size = 0.201)")
plt.ylim(0.65, 1.0)
plt.grid(axis='y', linestyle="--", alpha=0.7)

plt.show()