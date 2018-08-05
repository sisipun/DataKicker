from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def fit(x, y):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    log_regression = LogisticRegression(C=1)
    log_regression.fit(x_scaled, y)
    return log_regression
