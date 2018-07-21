from kicker_data import get_kicker_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

print('Decision Tree')

X_train, X_test, y_train, y_test = get_kicker_data()

tree = DecisionTreeClassifier(max_depth=4)
tree.fit(X_train, y_train)

tree_pred = tree.predict(X_test)
print(accuracy_score(y_test, tree_pred))

tree_params = {'max_depth': range(1, 20)}
tree_grid = GridSearchCV(tree, tree_params, cv=5)
tree_grid.fit(X_train, y_train)
print(tree_grid.best_params_, tree_grid.best_score_)
