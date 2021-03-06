#first step import dataset
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
# print iris.feature_names
# print iris.target_names
# print iris.data[0] #features values for first flowwer

#testing
test_idx = [0,50,100]
#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#3. Predict label for new flower
print test_target
print clf.predict(test_data)
#Goals
#1. import dataset
#2. Train a classifire
#3. Predict label for new flower
#4. Visualize the tree


import graphviz



dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris.pdf")
