import math
from kicker_data import get_kicker_data_with_date
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression, Ridge

print('Logistic Regression')

X_train, X_test, y_train, y_test = get_kicker_data_with_date()

log_regression = LogisticRegression(C=1)
log_regression.fit(X_train, y_train)
print(accuracy_score(y_test, log_regression.predict(X_test)))

rd = Ridge(alpha=1)
rd.fit(X_train, y_train)
predict = rd.predict(X_test)
print(accuracy_score(y_test, [math.fabs(round(i)) for i in predict]))
