# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:35:41 2021

@author: User
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#importing data set

dataset = pd.read_csv('Social_Network_ads.csv')

X = dataset.iloc[:, [2,3]].values
#X =X.reshape(-1,1)
Y = dataset.iloc[:,4].values
#Y = Y.reshape (-1,1)

from sklearn.cross_validation import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=.25 ,random_state = 0)


from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()

X = sc_X.fit_transform(X)


from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5 , metric='minkowski', p = 2)

classifier.fit(X_train,Y_train)

Y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test, Y_pred)

from matplotlib.colors import ListedColormap
X_set, Y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('knn Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show() 




