from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB



irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)


clf = GaussianNB()
clf.fit(x_train, y_train)
target_pred = clf.predict(x_test)
print(target_pred)

x = accuracy_score(y_test, target_pred, normalize = True)
print("hello",x)




