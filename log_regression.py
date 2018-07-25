from kicker_data import get_kicker_data, predict
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

print('Logistic Regression')

X_train, X_test, y_train, y_test = get_kicker_data()

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_regression = LogisticRegression(C=1)
log_regression.fit(X_train_scaled, y_train)
print(accuracy_score(y_test, log_regression.predict(X_test_scaled)))
print(predict(log_regression, 24, 4, 1, 2))
