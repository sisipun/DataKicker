from kicker_data import get_kicker_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

print('Random Forest')

X_train, X_test, y_train, y_test = get_kicker_data()

rf = RandomForestClassifier(7, max_features=32, random_state=17)
rf.fit(X_train, y_train)
forest_predictions = rf.predict(X_test)
print(accuracy_score(y_test, forest_predictions))

forest_params = {'max_depth': range(1, 21),
                 'max_features': range(30, 41)}

locally_best_forest = GridSearchCV(rf, forest_params, cv=5)
locally_best_forest.fit(X_train, y_train)
print(locally_best_forest.best_params_, locally_best_forest.best_score_)
