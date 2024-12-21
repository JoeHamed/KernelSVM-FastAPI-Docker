import numpy as np
import pandas as pd
import joblib

# Importing the dataset
dataset = pd.read_csv('./original_model/Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X_train)
print(y_train)
print(X_test)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)
print(X_test)

# Training the Kernel SVM model on the Training set
from sklearn import svm
classifier = svm.SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

# -----------------------------------------
# Save the model and the scaler
joblib.dump(classifier, './app/model.joblib')
joblib.dump(sc, './app/scaler.joblib')  # Save the scaler to use it during prediction


# Predicting a new result
print(f' Predicting the results for age of 30 and a salary of 87000 : {classifier.predict(sc.transform([[30, 87000]]))}')

# Predicting the Test set results
classifier.predict(X_test)
print(np.concatenate((classifier.predict(X_test).reshape(-1, 1), y_test.reshape(-1, 1)), 1))

# Making the confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, classifier.predict(X_test))
print(cm)
print(accuracy_score(y_test, classifier.predict(X_test)))

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10) # number of folds
print(f"Accuracy: {round(accuracies.mean()*100, 2)} %")
print(f"Standard Deviation: {round(accuracies.std()*100, 2)} %") # for the variance