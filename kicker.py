import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('kicker.csv')

y = df['red_won']
df.drop(['red_won', 'red_team_goals', 'yellow_team_goals'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['red_team_p1_id', 'red_team_p2_id', 'yellow_team_p1_id', 'yellow_team_p2_id'])
x = df.values

X_train, X_holdout, y_train, y_holdout = train_test_split(x, y, test_size=0.3, random_state=17)

tree = DecisionTreeClassifier(max_depth=4)
knn = KNeighborsClassifier(n_neighbors=15)

tree.fit(X_train, y_train)
knn.fit(X_train, y_train)

tree_pred = tree.predict(X_holdout)
print(accuracy_score(y_holdout, tree_pred))
knn_pred = knn.predict(X_holdout)
print(accuracy_score(y_holdout, knn_pred))

tree_params = {'max_depth': range(1, 20)}
tree_grid = GridSearchCV(tree, tree_params, cv=5)
tree_grid.fit(X_train, y_train)
print(tree_grid.best_params_, tree_grid.best_score_)

knn_params = {'n_neighbors': range(1, 20)}
knn_grid = GridSearchCV(knn, knn_params, cv=5)
knn_grid.fit(X_train, y_train)
print(knn_grid.best_params_, knn_grid.best_score_)

log_regression = LogisticRegression(C=1)
log_regression.fit(X_train, y_train)
print(accuracy_score(y_holdout, log_regression.predict(X_holdout)))
