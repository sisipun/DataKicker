from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def log_regression(x, y):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    lr = LogisticRegression(C=1)
    lr.fit(x_scaled, y)
    return lr
