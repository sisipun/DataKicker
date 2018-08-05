from data.kicker_data import get_kicker_split_data, get_prediction_data
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = get_kicker_split_data()

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_regression = LogisticRegression(C=1)
log_regression.fit(X_train_scaled, y_train)
print(accuracy_score(y_test, log_regression.predict(X_test_scaled)))

prediction = get_prediction_data(25, 11, 1, 3)
print(log_regression.predict(prediction))
