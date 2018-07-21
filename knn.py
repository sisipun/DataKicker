from kicker_data import get_kicker_data
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

print('KNN')

X_train, X_test, y_train, y_test = get_kicker_data()

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)
print(accuracy_score(y_test, knn_pred))

knn_params = {'n_neighbors': range(1, 20)}
knn_grid = GridSearchCV(knn, knn_params, cv=5)
knn_grid.fit(X_train, y_train)
print(knn_grid.best_params_, knn_grid.best_score_)